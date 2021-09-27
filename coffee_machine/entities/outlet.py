class Outlet:
    """Class for Outlet entity."""
    
    _count = 0

    @property
    def count(self) -> int:
        """Count property for Outlet class."""
        return self._count

    @count.setter
    def count(self, count: int) -> None:
        """
        Count setter for Outlet class
        
        Args:
            count(int): Count to set.

        Returns:
            None
        """
        self._count = count
