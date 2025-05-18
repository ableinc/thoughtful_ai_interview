import sys
from typing import Literal


DIMENSION_THRESHOLD: int = 150
VOLUME_THRESHOLD: int = 1_000_000
MASS_THRESHOLD: int = 20


def _calculate_volume(length: int, width: int, height: int) -> int:
    return length * width * height


def _is_valid_dimension(**kwargs) -> bool:
    if kwargs.get('length', None) is not None and kwargs['length'] >= DIMENSION_THRESHOLD:
        return False
    if kwargs.get('width', None) is not None and kwargs['width'] >= DIMENSION_THRESHOLD:
        return False
    if kwargs.get('height', None) is not None and kwargs['height'] >= DIMENSION_THRESHOLD:
        return False
    if kwargs.get('mass', None) is not None and kwargs['mass'] >= MASS_THRESHOLD:
        return False
    return True


def _is_valid_number(input: any) -> bool:
    if not isinstance(input, int) and not isinstance(input, str):
        return False
    try:
        int(input)
        return True
    except ValueError:
        return False


def sort(width: int, height: int, length: int, mass: int) -> Literal['STANDARD', 'SPECIAL', 'REJECTED']:
    is_bulky: bool = False
    is_heavy: bool = False
    # Validate inputs
    if not _is_valid_number(width) or not _is_valid_number(height) or not _is_valid_number(length) or not _is_valid_number(mass):
        return 'REJECTED'
    # Validate dimensions
    if not _is_valid_dimension(width=int(width), height=int(height), length=int(length)):
        is_bulky = True
    if not _is_valid_dimension(mass=int(mass)):
        is_heavy = True
    # Validate volume
    volumn: int = _calculate_volume(length=int(length), width=int(width), height=int(height))
    if volumn >= VOLUME_THRESHOLD:
        is_bulky = True
    # Dispatch
    if is_bulky and is_heavy:
        return 'REJECTED'
    if is_bulky or is_heavy:
        return 'SPECIAL'
    return 'STANDARD'
    

def main() -> None:
    args = sys.argv[1:]
    width = args[0]
    height = args[1]
    length = args[2]
    mass = args[3]
    dispatch_message: Literal['STANDARD', 'SPECIAL', 'REJECTED'] = sort(width, height, length, mass)
    print("Package is: ", dispatch_message)


if __name__ == '__main__':
    # start time: 2:20pm
    main()
    # stop time: 2:47pm

