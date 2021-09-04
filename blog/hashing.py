from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password:str):
        """Create hash password of any given String."""
        return pwd_context.hash(password)

    def verify(hashed_Pass,Plain_Pass):
        """Verify hash password with respected String."""
        return pwd_context.verify(Plain_Pass,hashed_Pass)