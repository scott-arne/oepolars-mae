# oepolars-mae

Maestro file format support for [oepolars](https://github.com/scott-arne/oepolars). Reads `.mae`, `.mae.gz`, and
`.maegz` files into Polars DataFrames following oepolars conventions.

**This only requires a valid OpenEye Toolkit license. You do not need to have any Schrodinger software installed.**

## Installation

Install as an oepolars extra:

```bash
pip install oepolars[mae]
```

Or install standalone:

```bash
pip install oepolars-mae
```

**Requirements:** Python 3.10+, oepolars >= 0.2.0, oemaestro >= 0.1.0, OpenEye Toolkits

## Quick Start

```python
import oepolars as oepl

df = oepl.read_mae("tests/assets/5.maegz")
print(df)
```

Prints:

```text
shape: (5, 16)
┌────────────┬───────────────┬─────┐
│ Molecule   ┆ Title         ┆ ... │
│ ---        ┆ ---           ┆     │
│ molecule   ┆ str           ┆     │
╞════════════╪═══════════════╪═════╡
│ <OEMol>    ┆ Aspirin       ┆ ... │
│ <OEMol>    ┆ Ibuprofen     ┆ ... │
│ <OEMol>    ┆ Acetaminophen ┆ ... │
│ <OEMol>    ┆ Caffeine      ┆ ... │
│ <OEMol>    ┆ Diazepam      ┆ ... │
└────────────┴───────────────┴─────┘
```

## Usage

### Column Naming

Rename the molecule and title columns, or suppress the title column entirely:

```python
import oepolars as oepl
df = oepl.read_mae("tests/assets/5.maegz", molecule_column="Mol", title_column="Name")
df = oepl.read_mae("tests/assets/5.maegz", no_title=True)
```

### Selecting Columns

Use `usecols` to include only specific data columns:

```python
df = read_mae("tests/assets/5.maegz", usecols=["NumAcceptors", "NumDonors"])
```

### Numeric Conversion

CT property values are strings by default. Use `numeric` to convert columns to Float64:

```python
# Convert a single column
df = read_mae("file.mae", numeric="pdb_tfactor")

# Convert multiple columns
df = read_mae("file.mae", numeric=["pdb_tfactor", "occupancy"])
```

### SMILES Columns

Add SMILES string columns alongside the molecule objects:

```python
df = oepl.read_mae("file.mae", add_smiles=True)
# Creates a "Molecule SMILES" column
```

### Conformer Grouping

Consecutive structures in a Maestro file can be grouped into multi-conformer molecules:

```python
df = read_mae("file.mae", conformer_test="absolute")
```

Available conformer tests:
- `"default"` -- groups consecutive molecules with matching titles
- `"absolute"` -- requires identical atom/bond ordering, properties, and title
- `"absolute_canonical"` -- requires matching canonical SMILES
- `"isomeric"` -- like absolute, but also requires matching stereochemistry
- `"omega"` -- like isomeric, plus invertible nitrogen stereochemistry

### Tag Formatting

Maestro property keys follow a `type_owner_name` convention (e.g., `r_pdb_PDB_CRYST1_a`). By default, only the name portion is used as the column name. Control this with `tags`:

```python
import oepolars as oepl
from oepolars_mae import TAG_ALL, TAG_NAME, TAG_NONE

# Default: clean names only (e.g., "PDB_CRYST1_a")
df = oepl.read_mae("file.mae")

# Full Maestro keys (e.g., "r_pdb_PDB_CRYST1_a")
df = oepl.read_mae("file.mae", tags=TAG_ALL)

# No data columns (molecules and titles only)
df = oepl.read_mae("file.mae", tags=TAG_NONE)
```

### Perception Control

Control post-parse chemical perception with the `perception` parameter:

```python
from oepolars_mae import read_mae, PERCEPTION_NONE

df = oepl.read_mae("file.mae", perception=PERCEPTION_NONE)
```

By default, only limited molecule perception occurs in order to respect what is specified in the Maestro file.

### Configuration Object

For repeated use, pass an `OEMaestroReaderConfig` object. Keyword arguments override config values:

```python
from oepolars_mae import read_mae, OEMaestroReaderConfig, TAG_ALL

config = OEMaestroReaderConfig()
config.tags = TAG_ALL

df = oepl.read_mae("file.mae", config=config)
df = oepl.read_mae("file.mae", config=config, tags=TAG_NAME)  # tags overrides config
```

## License

MIT
