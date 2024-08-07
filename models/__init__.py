#!/usr/bin/python3
"""Initializes package level variables"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()