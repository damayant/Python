"""Common code smells and anti-patterns to avoid.

This module demonstrates BAD practices that should be avoided.
"""

# ❌ BAD: Magic numbers without explanation
def calculate_age_bad(birth_year):
    """Calculate age from birth year (using magic number)."""
    return 2024 - birth_year  # What is 2024? Bad practice


# ✓ GOOD: Named constant
from datetime import datetime

CURRENT_YEAR = datetime.now().year

def calculate_age_good(birth_year):
    """Calculate age from birth year (using named constant)."""
    return CURRENT_YEAR - birth_year


# ❌ BAD: God object with too many responsibilities
class BadUserManager:
    """Does everything - violates Single Responsibility Principle."""

    def create_user(self, username, password):
        """Create user."""
        pass

    def send_email(self, email, message):
        """Send email."""
        pass

    def log_activity(self, activity):
        """Log activity."""
        pass

    def calculate_stats(self, data):
        """Calculate statistics."""
        pass

    def backup_database(self):
        """Backup database."""
        pass


# ✓ GOOD: Separate concerns into different classes
class GoodUserManager:
    """Only manages users."""

    def create_user(self, username, password):
        """Create user."""
        pass


class EmailService:
    """Handles email operations."""

    def send_email(self, email, message):
        """Send email."""
        pass


# ❌ BAD: Deep nesting (arrow anti-pattern)
def process_data_bad(data):
    """Nested if statements make code hard to read."""
    if data:
        if isinstance(data, list):
            if len(data) > 0:
                for item in data:
                    if item:
                        if item.get("active"):
                            return item
    return None


# ✓ GOOD: Early returns to reduce nesting
def process_data_good(data):
    """Use early returns to flatten nesting."""
    if not data or not isinstance(data, list) or not data:
        return None

    for item in data:
        if item and item.get("active"):
            return item

    return None


# ❌ BAD: Mutable default arguments
def add_to_list_bad(item, target_list=[]):
    """NEVER use mutable defaults - list is shared across calls."""
    target_list.append(item)
    return target_list


# ✓ GOOD: Use None as default and create new list
def add_to_list_good(item, target_list=None):
    """Use None as default for mutable objects."""
    if target_list is None:
        target_list = []
    target_list.append(item)
    return target_list


# ❌ BAD: Bare except clauses
def load_config_bad():
    """Catching all exceptions hides bugs."""
    try:
        config = {}
        # Some code
        return config
    except:  # Catches everything including KeyboardInterrupt!
        return None


# ✓ GOOD: Specific exception handling
def load_config_good():
    """Handle specific exceptions."""
    try:
        config = {}
        # Some code
        return config
    except FileNotFoundError:
        return None
    except (KeyError, ValueError):
        return None


# ❌ BAD: Type checking with isinstance in multiple places
def process_value_bad(value):
    """Repeated type checks - violates DRY principle."""
    if isinstance(value, str):
        return value.upper()
    elif isinstance(value, int):
        return value * 2
    elif isinstance(value, list):
        return len(value)
    else:
        return None


# ✓ GOOD: Use polymorphism or dispatch pattern
def process_string(value):
    """Process string value."""
    return value.upper()

def process_int(value):
    """Process integer value."""
    return value * 2

def process_list(value):
    """Process list value."""
    return len(value)


# ❌ BAD: Inconsistent naming and style
class BadStyleClass:
    """Inconsistent naming conventions."""

    def __init__(self):
        self.name = None
        self.user_id = None
        self._InternalVar = None
        self.DATA = "private"  # Looks like constant but isn't


# ✓ GOOD: Consistent naming
class GoodStyleClass:
    """Consistent naming following PEP 8."""

    # Class constants in UPPER_CASE
    DEFAULT_TIMEOUT = 30

    def __init__(self):
        # Instance variables in snake_case
        self.name = None
        self.user_id = None
        # Private variables with underscore prefix
        self._internal_var = None


# ❌ BAD: Very long functions that do too much
def bad_process_user_data(user_dict, database, email_service, logger):
    """Does too many things - hard to test and maintain."""
    try:
        if not user_dict:
            return False

        user_dict["processed_at"] = datetime.now()

        if "email" in user_dict:
            email = user_dict["email"]
            if "@" not in email:
                logger.error(f"Invalid email: {email}")
                return False

        database.save(user_dict)

        if user_dict.get("send_welcome"):
            email_service.send(
                user_dict["email"],
                "Welcome!"
            )

        logger.info(f"User processed: {user_dict['name']}")
        return True

    except Exception as e:
        logger.error(f"Error: {e}")
        return False


# ✓ GOOD: Break into smaller, focused functions
def validate_user_data(user_dict):
    """Validate user data."""
    if not user_dict:
        return False
    if "email" in user_dict and "@" not in user_dict["email"]:
        return False
    return True

def save_user_to_database(user_dict, database):
    """Save user to database."""
    user_dict["processed_at"] = datetime.now()
    database.save(user_dict)

def send_welcome_email_if_needed(user_dict, email_service):
    """Send welcome email if requested."""
    if user_dict.get("send_welcome"):
        email_service.send(user_dict["email"], "Welcome!")

def process_user_data_good(user_dict, database, email_service, logger):
    """Orchestrate user processing with focused functions."""
    try:
        if not validate_user_data(user_dict):
            return False

        save_user_to_database(user_dict, database)
        send_welcome_email_if_needed(user_dict, email_service)

        logger.info(f"User processed: {user_dict.get('name')}")
        return True

    except Exception as e:
        logger.error(f"Error processing user: {e}")
        return False


# ❌ BAD: No documentation
def calc(x, y, z):
    """Vague function name and no docstring."""
    return x * y + z


# ✓ GOOD: Clear name and documentation
def calculate_total_cost(unit_price, quantity, tax_rate):
    """Calculate total cost including tax.

    Args:
        unit_price: Price per unit
        quantity: Number of units
        tax_rate: Tax rate as decimal (e.g., 0.1 for 10%)

    Returns:
        Total cost including tax
    """
    subtotal = unit_price * quantity
    tax = subtotal * tax_rate
    return subtotal + tax


# ❌ BAD: Silent failures
def get_user_age_bad(user_dict):
    """Silently returns None on error."""
    try:
        return 2024 - user_dict["birth_year"]
    except:
        return None


# ✓ GOOD: Informative errors
def get_user_age_good(user_dict):
    """Return age with proper error handling.

    Args:
        user_dict: User dictionary

    Returns:
        User age

    Raises:
        KeyError: If birth_year is missing
        TypeError: If birth_year is not numeric
    """
    if "birth_year" not in user_dict:
        raise KeyError("User dictionary missing 'birth_year' field")

    birth_year = user_dict["birth_year"]
    if not isinstance(birth_year, int):
        raise TypeError(f"birth_year must be int, got {type(birth_year).__name__}")

    return CURRENT_YEAR - birth_year

