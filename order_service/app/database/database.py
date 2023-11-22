from asyncio import current_task
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine, async_sessionmaker, \
    async_scoped_session

from order_service.app.core.config import settings


class DatabaseHelper:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(url=url,
                                          echo=echo)
        self.session_factory = async_sessionmaker(bind=self.engine,
                                                  autoflush=False,
                                                  autocommit=False,
                                                  expire_on_commit=False)

    def get_scope_session(self):
        session = async_scoped_session(session_factory=self.session_factory,
                                       scopefunc=current_task)
        return session

    async def session_dependency(self) -> AsyncSession:
        """Create session for every request."""
        async with self.session_factory() as session:
            # use yield in order not to close session after leave the context
            yield session
            await session.close()

    async def scope_session_dependency(self) -> AsyncSession:
        """Create session with a limited scope.Enable sharing within a current task"""
        session = self.get_scope_session()
        # use yield in order not to close session after leave the context
        yield session
        await session.close()


db_helper = DatabaseHelper(url=settings.db_url, echo=True)
