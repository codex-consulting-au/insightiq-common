# Versioning Guide

This package follows [Semantic Versioning](https://semver.org/) (SemVer 2.0.0).

## Version Format

`MAJOR.MINOR.PATCH` (e.g., `1.2.3`)

- **MAJOR**: Incompatible API changes
- **MINOR**: New backward-compatible functionality
- **PATCH**: Backward-compatible bug fixes

## How to Update Version

1. Update the `VERSION` file with the new version number
2. Document changes in `CHANGELOG.md`
3. Commit changes: `git commit -am "Bump version to x.y.z"`
4. Create a git tag: `git tag vx.y.z`
5. Push tag: `git push --tags`

## Installation

Services can install specific versions:

```bash
# Latest version from main branch
pip install "git+https://github.com/<ORG>/<REPO>.git#subdirectory=insightiq_common"

# Specific version tag
pip install "git+https://github.com/<ORG>/<REPO>.git@v0.1.0#subdirectory=insightiq_common"

# Specific branch
pip install "git+https://github.com/<ORG>/<REPO>.git@feature-branch#subdirectory=insightiq_common"
```

## Best Practices

- Always pin to a specific version tag in production
- Use version ranges in development: `insightiq-common>=0.1.0,<1.0.0`
- Test new versions in staging before updating production

