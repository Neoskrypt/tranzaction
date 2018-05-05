
class BaseError(Exception):
    def __init__(self,reason:str):
        self._reason = reason


class CommitError(BaseError):
    def __init__(self):
        super().__init__()
    def __str__(self):

        return ("Commit Error:\n".join("%s=>%s" % i for i in self._reason))


class RollbackError(BaseError):
    def __init__(self):
        super().__init__()
    def __str__(self):

        return ("Rollback Error:\n".join("%s=>%s" % i for i in self._reason))
