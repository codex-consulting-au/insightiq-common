# InsightIQ Common

Shared context providers for InsightIQ services.

## Installation

### Method 1: Direct Git Install

```bash
pip install "git+ssh://git@bitbucket.org/codex_data/insightiq_common.git@v0.1.0"
```

Replace `v0.1.0` with the desired version tag.

### Method 2: In requirements.txt

```txt
insightiq-common @ git+ssh://git@bitbucket.org/codex_data/insightiq_common.git@v0.1.0
```

### Method 3: In pyproject.toml

```toml
dependencies = [
    "insightiq-common @ git+ssh://git@bitbucket.org/codex_data/insightiq_common.git@v0.1.0"
]
```

### Method 4: Local Development Install

For local development with editable install:

```bash
git clone git@bitbucket.org:codex_data/insightiq_common.git
cd insightiq_common
pip install -e .
```

Or with development dependencies:

```bash
pip install -e ".[dev]"
```

## Overview

This package provides base classes for implementing context providers:

- **Schema Context Providers**: Generate context from database schema information
- **Semantic Context Providers**: Generate context from natural language queries

## Usage

### Schema Context Provider

```python
from insightiq_common.context_providers.schema_context_provider import (
    BaseSchemaContextProvider,
)
from insightiq_common.models.context_providers.schema_context_provider import (
    SchemaContextProviderInput,
    SchemaContextProviderOutput,
)

class MySchemaProvider(BaseSchemaContextProvider):
    def __init__(self):
        super().__init__(
            name="MySchemaProvider",
            description="Your provider description"
        )
    
    def get_context(self, input_data: SchemaContextProviderInput) -> SchemaContextProviderOutput:
        # Your implementation
        return SchemaContextProviderOutput(context="...")
```

### Semantic Context Provider

```python
from insightiq_common.context_providers.semantic_context_provider import (
    BaseSemanticContextProvider,
)
from insightiq_common.models.context_providers.semantic_context_provider import (
    SemanticContextProviderInput,
    SemanticContextProviderOutput,
)

class MySemanticProvider(BaseSemanticContextProvider):
    def __init__(self):
        super().__init__(
            name="MySemanticProvider",
            description="Your provider description"
        )
    
    def get_context(self, input_data: SemanticContextProviderInput) -> SemanticContextProviderOutput:
        # Your implementation
        return SemanticContextProviderOutput(context="...", tables_used=[])
```

## Examples

See the `examples/` directory for complete working examples.

## Requirements

- Python >= 3.9
- pydantic >= 2.0.0

## Development

### Setup

Clone the repository and install in editable mode with development dependencies:

```bash
git clone git@bitbucket.org:codex_data/insightiq_common.git
cd insightiq_common
pip install -e ".[dev]"
```

### Code Formatting

Format code with black:

```bash
black .
```

Lint with ruff:

```bash
ruff check .
```

Auto-fix issues:

```bash
ruff check --fix .
```

### Type Checking

Run mypy for type checking:

```bash
mypy insightiq_common
```

### Development Workflow

1. Make your changes on a feature branch
2. Run tests: `pytest`
3. Format code: `black .`
4. Check linting: `ruff check .`
5. Check types: `mypy insightiq_common`
6. Commit your changes

### Releasing a New Version

All consuming repos (`insightiq_core`, `visualisation_agent`, `insightiq_services`) reference `insightiq-common` by **git tag**. To release a new version:

1. Merge your feature branch into `master`
2. Tag the release on master:
   ```bash
   git checkout master
   git pull
   git tag v1.x.x
   git push origin v1.x.x
   ```
3. Update the tag reference in each consuming repo's `pyproject.toml`:
   ```toml
   insightiq-common = { git = "https://bitbucket.org/codex_data/insightiq_common.git", tag = "v1.x.x" }
   ```
4. Run `uv sync` in each consuming repo to pull the new version

> **Important:** Do not point consuming repos at feature branches for production use. Always merge to `master` and tag.

