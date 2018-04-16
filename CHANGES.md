# Change Log

All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

## [UNRELEASED] [0000-00-00]
#### Added
 - Feature: generate a markov chain from all collected text by using `!markov`

## [0.1.3] [2018-04-05]
#### Fixed
 - Changed how get_* functions return so that they no longer crash the legobot core

#### Added
 - Slightly improved logging. Very slightly. Like, I just added a single info statement kind of slightly.

## [0.1.2] [2018-04-03]
#### Changed
 - Changed MarkovListener to use new `metadata['display_name']` (from Legobot 1.2.1+) for redis keys instead of `metadata['source_user']`.

## [0.1.1] [2018-04-03]
#### Added
 - Legos now return `None` for get_help and get_name. Stealth mode, yo.
   - This may or may not be a good idea.

#### Fixed
 - Set minimum Legobot verion to 1.2.1 to use improved metadata fields

## [0.1.0] [2018-03-29]
### Added
 - MarkovListener
 - MarkovGenerator
