# Unified Schema Ecosystem for IGS Metadata

This repo contains a (draft) ecosystem of interrelated JSON Schema documents comprising a framework for the formal description of heterogeneous experimental metadata generated by different data sources.

## Critical mission concepts
* The central architecture for this system consists of a **core set of JSON Schemas** describing five fundamental object types: **sample, subject, study, event** and **file**. The core schema set lays out **metadata likely to be shared across all objects of each of these five types**, regardless of source, project or specific context.
* A mechanism has been created for the system-wide specification of **controlled vocabularies (CVs)**, to be applied to selected metadata fields, so as to constrain valid usage.
* Support is provided for the creation of **subcollection-specific extension schemas**, so as to facilitate the storage of idiomatic metadata (not modeled by the universal core schema set) attached to particular data subcollections (e.g. the creation of separate extensions will allow for fuller descriptions of HMP data, VMRC data, NeMO data, etc.).
* Support is also provided for the creation of **subtype schemas**, to model more specific (but still generally applicable) metadata derived from the five core types (e.g. "mouse" and "human" extensions might be built on top of the core "subject" schema, describing species-specific metadata in each extension).
* The core schema set must be kept structurally and conceptually simple at all times, to facilitate both onboarding of new data providers and also ongoing ETL work within IGS. **Inherent schema complexity must not constitute a roadblock** that delays or prevents the rapid construction of valid (schema-conformant) metadata sets.
