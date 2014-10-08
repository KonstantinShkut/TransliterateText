#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sublime
import sublime_plugin


class TransliterateTextCommand(sublime_plugin.TextCommand):

    def run(self, edit, dictionary_file):
        s = sublime.load_settings(dictionary_file)
        dictionary = s.get('chars_mapping')

        # Some text selected
        if not self.view.sel()[0].empty():

            selections = self.view.sel()
            for sel in selections:
                selection_text = self.view.substr(sel)
                self.view.replace(edit, sel, self.transliterateText(selection_text, dictionary))

        # Nothing selected
        else :

            # Get entire view
            # region = sublime.Region(0, self.view.size())
            sel = sublime.Region(0, self.view.size())
            selection_text = self.view.substr(sel)
            self.view.replace(edit, sel, self.transliterateText(selection_text, dictionary))

    def transliterateText(self, input_string, dictionary):
        translit_string = []
        for char in input_string:
            translit_string.append(dictionary.get(char, char))
        return ''.join(translit_string)
