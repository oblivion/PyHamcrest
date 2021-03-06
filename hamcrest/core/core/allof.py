from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.helpers.wrap_matcher import wrap_matcher

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class AllOf(BaseMatcher):
    """Calculates the logical conjunction of multiple matchers.

    Evaluation is shortcut, so subsequent matchers are not called if an earlier
    matcher returns ``False``.

    """

    def __init__(self, *matchers):
        self.matchers = matchers

    def matches(self, item, mismatch_description=None):
        for matcher in self.matchers:
            if not matcher.matches(item):
                if mismatch_description:
                    mismatch_description.append_description_of(matcher) \
                                        .append_text(' ')
                    matcher.describe_mismatch(item, mismatch_description)
                return False
        return True

    def describe_mismatch(self, item, mismatch_description):
        self.matches(item, mismatch_description)

    def describe_to(self, description):
        description.append_list('(', ' and ', ')', self.matchers)


def all_of(*items):
    """Evaluates to ``True`` only if *all* of the passed in matchers evaluate
    to ``True``.

    :param items: Each item is a matcher, or a value for
        :py:func:`~hamcrest.core.core.isequal.equal_to` matching.

    """
    return AllOf(*[wrap_matcher(item) for item in items])
