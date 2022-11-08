# Another Best Starting Word program

This program is another simple attempt to find the best starting word in
Wordle.

It iterates through a dictionary and applies scores for each five-letter word.
Words that don't have exactly five letters are not considered for scores at
all.

Points are awarded to words for each letter. A letter earns points for each
time it letter appears in a five-letter word, including itself, and it earns
additional points for each time it appears in a five-letter word in the same
position (index), again including itself.

For example, consider a dictionary with only these three words. If 1 point is
awarded for each time a letter appears in a word (including itself), and an
extra _1_ point is awarded each time a letter appears in the same position in a
word (including itself), the scores would be as follows:

* `bleat` = 1 + _1_ + 1 + _1_ + 2 + _2_ + 2 + _1_ + 2 + _2_ = **15**
* `quack` = 1 + _1_ + 1 + _1_ + 2 + _1_ + 1 + _1_ + 1 + _1_ = **11**
* `tweet` = 2 + _1_ + 1 + _1_ + 2 + _2_ + 2 + _1_ + 2 + _2_ = **16**

According to this example, when words are scored this way, _tweet_ would be the
best starting word for this dictionary.

## Results

When words are scored as in the example above, i.e. `LETTER_USED_MULTIPLIER =
1` and `LETTER_IN_PLACE_MULTIPLIER = 1`, with a real dictionary, the 10 best
starting words are:

* `hares` 17069
* `mares` 17089
* `bares` 17116
* `pares` 17226
* `cares` 17355
* `lanes` 17383
* `tales` 17405
* `dares` 17451
* `rates` 17536
* `tares` 17873

If we add more weight to letters in their position, i.e.
`LETTER_USED_MULTIPLIER = 1` and `LETTER_IN_PLACE_MULTIPLIER = 3`, the 10 best
starting words are:

* `rates` 28226
* `mares` 28283
* `canes` 28304
* `lanes` 28453
* `tales` 28529
* `bares` 28568
* `pares` 28606
* `dares` 28673
* `cares` 28831
* `tares` 29237

But since Wordle doesn't usually include conjugated words, we've added code to
remove words ending in S, D or 'er' from consideration. In that case, with
`LETTER_USED_MULTIPLIER = 1` and `LETTER_IN_PLACE_MULTIPLIER = 3`, the 10 best
starting words are:

* `crane` 8322
* `crate` 8322
* `raise` 8345
* `sauce` 8442
* `shale` 8453
* `snare` 8458
* `share` 8487
* `stale` 8487
* `stare` 8521
* `slate` 8799

We may decide that we don't care about the `LETTER_USED_MULTIPLIER` at all,
because a common letter _not_ being in a word narrows down the possibilities as
well. So, with `LETTER_USED_MULTIPLIER = 0` and `LETTER_IN_PLACE_MULTIPLIER =
1`, the 10 best starting words are:

* `shale` 1550
* `slice` 1551
* `saucy` 1559
* `suite` 1559
* `souse` 1560
* `slate` 1566
* `soapy` 1566
* `sauce` 1587
* `sooty` 1589
* `saree` 1619
