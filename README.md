# Flutter pubspec.yaml updater

![Python](https://img.shields.io/badge/-Python-ffff47?style=flat-square&logo=python)

A simple tool that updates your *pubspec.yaml* file, of a Flutter project, without altering the structure of your file.

## Install

Just run `INSTALL.sh`, this will add the command `pubspec_update` in your terminal.

## Usage

Run `pubspec_update` passing an empty argument or, alternatively, either the path of the Flutter project or the *pubspec.yaml* file. Example:

- `pubspec_update`, this will take as path the current working directory.
- `pubspec_update ~/my/flutter/project`
- `pubspec_update ~/my/flutter/project/pubspec.yaml`

The tool will print a table with all the packages that need an update. This table contains the package name, the current version in the *pubspec* and the newer version available on [pub.dev](https://pub.dev).

![1](README_images/1.png)

Immediately after, two questions will be asked:

- Whether you want the tool to open the browser on the changelog page of every package.
- Whether you want the tool to automatically update the `pubspec.yaml` file without altering the file structure at all — like comments, package orders, etc.

Enjoy!
