#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/testing")

class BoostMplConan(base.BoostBaseConan):
    name = "boost_mpl"
    version = "1.69.0"
    url = "https://github.com/bincrafters/conan-boost_mpl"
    lib_short_names = ["mpl"]
    header_only_libs = ["mpl"]
    b2_requires = [
        "boost_config",
        "boost_core",
        "boost_predef",
        "boost_preprocessor",
        "boost_static_assert",
        "boost_type_traits",
        "boost_utility"
    ]
