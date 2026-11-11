# A self-documenting Makefile. Run `make help` for the list of targets.
# All Python tooling is managed with uv (https://docs.astral.sh/uv/).

SCHEMA := OCX_ext_rudder.xsd
XSDATA_CONFIG := ocx_rudder/.xsdata.xml

# SETUP ########################################################################
sync: ## Create/update the virtual environment with all dependencies
	uv sync
.PHONY: sync

# GENERATE DATABINDINGS ########################################################
generate: ## Generate the python data-bindings. See ocx_rudder/.xsdata.xml for xsdata settings
	uv run xsdata generate $(SCHEMA) --config $(XSDATA_CONFIG)
.PHONY: generate

# TESTS #######################################################################
test: ## Run the tests
	uv run pytest
.PHONY: test

# CHECKS ######################################################################
lint: ## Run the ruff formatter check and linter
	uv run ruff format --check .
	uv run ruff check .
.PHONY: lint

# BUILD #######################################################################
build: ## Build a distribution of the package
	uv build
.PHONY: build

# RELEASE #####################################################################
bump: ## Bump the version, regenerate bindings and tag, e.g. `make bump VERSION=1.3.0`
	uv run tbump $(VERSION)
.PHONY: bump

# HELP ########################################################################
help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
.PHONY: help

.DEFAULT_GOAL := help