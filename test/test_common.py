import unittest

from buildbotcustom.common import normalizeName


class TestNormalizeName(unittest.TestCase):
    def testNoPrefix(self):
        self.assertEquals(normalizeName('mozilla-beta'), 'm-beta')

    def testPrefix(self):
        self.assertEquals(normalizeName('comm-release', product='thunderbird'), 'tb-c-rel')

    def testExclusiveWordReplacement(self):
        self.assertEquals(normalizeName('spidermonkey-errasdebug'), 'spidermonkey-errasdebug')
