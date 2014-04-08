#!/usr/bin/perl
#
# An isogram (also known as a "nonpattern word") is a logological term
# for a word or phrase without a repeating letter. It is also used by
# some to mean a word or phrase in which each letter appears the same
# number of times, not necessarily just
# once. (http://en.wikipedia.org/wiki/Isogram)
# Examples:
#   'Wyoming' is an isogram, while 'Alabama' is not.
#   'Many' and 'few' are isograms, 'none' is not.
#   'Toto' is an isogram by the second definition, but not the first.
# Requirement: Given a word or phrase, report whether or not it's an
# isogram by the first definition above. Bonus: test for the second
# definition.
#
# Wyoming Alabama Many few none Toto Dermatoglyphics
#

sub isIsogram {
    my ($word) = @_;
    my %letterCounts = (); # Try commenting out this line or removing the "my".
    foreach (split //, $word) {
        # Unlike list arrays the index is enclosed in curly braces,
        # the idea being that associative arrays are fancier than list
        # arrays.
        $letterCounts{lc()}++;
    }
    my ($minCount, $maxCount) = (sort { $a <=> $b } values %letterCounts)[0,-1];
        if ($minCount != $maxCount) {
    return "no"
        } elsif ($minCount == 1) {
    return "yes"
        } else {
    return "alt"
        }
}

sub printAnswer {
    my ($word) = @_;
    $answer = isIsogram $word;
    print "$word $answer\n";
}

if ($#ARGV >= 0 && $ARGV[0] =~ "(-s|--stats)") {
    shift(@ARGV);
    my %stats;
}

# I give up playing in this cesspool.

printAnswer "Wyoming";
printAnswer "Alabama";
printAnswer "Many";
printAnswer "few";
printAnswer "none";
printAnswer "Toto";
printAnswer "Dermatoglyphics";
