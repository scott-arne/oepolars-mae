"""Compatibility layer for oepolars internal imports and oemaestro re-exports.

Centralizes dependencies on oepolars private API so there is exactly one place
to update if oepolars refactors its internals.
"""
from oemaestro import (
    PERCEPTION_ALL,
    PERCEPTION_BOND_ORDERS,
    PERCEPTION_CONNECTIVITY,
    PERCEPTION_DEFAULT,
    PERCEPTION_FORMAL_CHARGES,
    PERCEPTION_IMPLICIT_HYDROGENS,
    PERCEPTION_NONE,
    PERCEPTION_RINGS,
    TAG_ALL,
    TAG_NAME,
    TAG_NONE,
    TAG_OWNER,
    TAG_TYPE,
    MaestroMol,
    MaestroReader,
    MolConverter,
    OEMaestroReader,
    OEMaestroReaderConfig,
)

__all__ = [
    "TAG_NONE",
    "TAG_TYPE",
    "TAG_OWNER",
    "TAG_NAME",
    "TAG_ALL",
    "PERCEPTION_NONE",
    "PERCEPTION_CONNECTIVITY",
    "PERCEPTION_RINGS",
    "PERCEPTION_BOND_ORDERS",
    "PERCEPTION_IMPLICIT_HYDROGENS",
    "PERCEPTION_FORMAL_CHARGES",
    "PERCEPTION_DEFAULT",
    "PERCEPTION_ALL",
    "OEMaestroReaderConfig",
    "OEMaestroReader",
    "MaestroReader",
    "MaestroMol",
    "MolConverter",
]
