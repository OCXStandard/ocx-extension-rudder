# ocx-extension-rudder: Changelog

## Unreleased
### Fixed
 - ``ocxRU:ForgedMaterial`` now uses ``ForgedMaterial_T`` instead of ``CastedMaterial_T``.
 - Align version strings, schema namespace (``V120``) and ``schemaVersion`` with the 1.2.0 release.
 - Fix the tbump data-binding generation steps and the generated package naming.
### Changed
 - Migrate Python tooling from Poetry/conda to uv.
 - Remove the generated XMLSpy documentation (``docs/XML``) from the repository.
 - Add tests and a GitHub Actions CI workflow.

## 1.2.0 - 2023-07-17
### Changed
Fix wrong base version for ocxRU:Nut

## 1.1.0 - 2023-06-27
### Documentation
 - Update XML Spy html documentation.
### Changed
 - Change ocxRU target namespace in schema. 
 - Bump version 1.0.0 -> 1.1.0


## 1.0.0 - 2023-06-27
### 1st release 
 - Bump version 0.1.0 -> 1.0.0

## 0.1.0 - 2023-06-12
### Added 
- Add new elements and attributes [(1249671)](https://github.com/OCXStandard/ocx-extension-rudder/commit/1249671c3db6e211d5c47f9a91ff0ff3c5846399)
- Add ``DesignView`` to the ``RudderDocument``

## 0.1.0 - 2023-05-01

### Documentation
- Add XMLSpy documentation [(6285026)](https://github.com/OCXStandard/ocx-extension-rudder/commit/62850264e94abe317bc500b9a93a3a9ea60eda09)

## 0.1.0 - 2023-04-20
### Added
- First commit [(11fe2be)](https://github.com/OCXStandard/ocx-extension-rudder/commit/11fe2be546cdac3a5e755787fc972752367ca9a4)
