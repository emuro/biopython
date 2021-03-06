# Copyright 2004 by Frank Kauff.  All rights reserved.
# Revisions copyright 2008-2013 by Peter Cock. All rights reserved.
# Revisions copyright 2009-2009 by Michiel de Hoon. All rights reserved.
# This code is part of the Biopython distribution and governed by its
# license.  Please see the LICENSE file that should have been included
# as part of this package.

"""Tests for Ace module."""

import unittest

from Bio.Sequencing import Ace


class AceTestOne(unittest.TestCase):
    def setUp(self):
        self.handle = open("Ace/contig1.ace")

    def tearDown(self):
        self.handle.close()

    def test_check_ACEParser(self):
        """Test to check that ACEParser can parse the whole file into one record."""
        record = Ace.read(self.handle)
        self.assertEqual(record.ncontigs, 2)
        self.assertEqual(record.nreads, 16)
        self.assertEqual(len(record.wa), 1)
        self.assertEqual(record.wa[0].tag_type, "phrap_params")
        self.assertEqual(record.wa[0].program, "phrap")
        self.assertEqual(record.wa[0].date, "040203:114710")
        self.assertEqual(
            record.wa[0].info,
            [
                "phrap 304_nuclsu.fasta.screen -new_ace -retain_duplicates",
                "phrap version 0.990329",
            ],
        )
        self.assertEqual(len(record.contigs), 2)
        self.assertEqual(len(record.contigs[0].reads), 2)
        self.assertEqual(record.contigs[0].name, "Contig1")
        self.assertEqual(record.contigs[0].nbases, 856)
        self.assertEqual(record.contigs[0].nreads, 2)
        self.assertEqual(record.contigs[0].nsegments, 31)
        self.assertEqual(record.contigs[0].uorc, "U")
        center = len(record.contigs[0].sequence) // 2
        self.assertEqual(record.contigs[0].sequence[:10], "aatacgGGAT")
        self.assertEqual(
            record.contigs[0].sequence[center - 5 : center + 5], "ACATCATCTG"
        )
        self.assertEqual(record.contigs[0].sequence[-10:], "cATCTAGtac")
        center = len(record.contigs[0].quality) // 2
        self.assertEqual(
            record.contigs[0].quality[:10], [0, 0, 0, 0, 0, 0, 22, 23, 25, 28]
        )
        self.assertEqual(
            record.contigs[0].quality[center - 5 : center + 5],
            [90, 90, 90, 90, 90, 90, 90, 90, 90, 90],
        )
        self.assertEqual(
            record.contigs[0].quality[-10:], [15, 22, 30, 24, 28, 22, 21, 15, 19, 0]
        )
        self.assertEqual(len(record.contigs[0].af), 2)
        self.assertEqual(record.contigs[0].af[1].name, "BL060c3-LR0R.b.ab1")
        self.assertEqual(record.contigs[0].af[1].coru, "U")
        self.assertEqual(record.contigs[0].af[1].padded_start, 1)
        self.assertEqual(len(record.contigs[0].bs), 31)
        self.assertEqual(record.contigs[0].bs[15].name, "BL060c3-LR5.g.ab1")
        self.assertEqual(record.contigs[0].bs[15].padded_start, 434)
        self.assertEqual(record.contigs[0].bs[15].padded_end, 438)
        self.assertEqual(record.contigs[0].bs[30].name, "BL060c3-LR0R.b.ab1")
        self.assertEqual(record.contigs[0].bs[30].padded_start, 823)
        self.assertEqual(record.contigs[0].bs[30].padded_end, 856)
        self.assertEqual(len(record.contigs[0].ct), 1)
        self.assertEqual(record.contigs[0].ct[0].name, "Contig1")
        self.assertEqual(record.contigs[0].ct[0].tag_type, "repeat")
        self.assertEqual(record.contigs[0].ct[0].program, "phrap")
        self.assertEqual(record.contigs[0].ct[0].padded_start, 52)
        self.assertEqual(record.contigs[0].ct[0].padded_end, 53)
        self.assertEqual(record.contigs[0].ct[0].date, "555456:555432")
        self.assertEqual(
            record.contigs[0].ct[0].info,
            ["This is the first line of comment for c1", "and this the second for c1"],
        )
        self.assertIsNone(record.contigs[0].wa)
        self.assertEqual(len(record.contigs[0].reads), 2)
        self.assertEqual(record.contigs[0].reads[0].rd.name, "BL060c3-LR5.g.ab1")
        self.assertEqual(record.contigs[0].reads[0].rd.padded_bases, 868)
        self.assertEqual(record.contigs[0].reads[0].rd.info_items, 0)
        self.assertEqual(record.contigs[0].reads[0].rd.read_tags, 0)
        center = len(record.contigs[0].reads[0].rd.sequence) // 2
        self.assertEqual(record.contigs[0].reads[0].rd.sequence[:10], "tagcgaggaa")
        self.assertEqual(
            record.contigs[0].reads[0].rd.sequence[center - 5 : center + 5],
            "CCGAGGCCAA",
        )
        self.assertEqual(record.contigs[0].reads[0].rd.sequence[-10:], "gaaccatcag")
        self.assertEqual(record.contigs[0].reads[0].qa.qual_clipping_start, 80)
        self.assertEqual(record.contigs[0].reads[0].qa.qual_clipping_end, 853)
        self.assertEqual(record.contigs[0].reads[0].qa.align_clipping_start, 22)
        self.assertEqual(record.contigs[0].reads[0].qa.align_clipping_end, 856)
        self.assertIsNone(record.contigs[0].reads[0].ds)
        self.assertEqual(len(record.contigs[0].reads[0].rt), 4)
        self.assertEqual(record.contigs[0].reads[0].rt[0].name, "BL060c3-LR5.g.ab1")
        self.assertEqual(
            record.contigs[0].reads[0].rt[0].tag_type, "matchElsewhereHighQual"
        )
        self.assertEqual(record.contigs[0].reads[0].rt[0].program, "phrap")
        self.assertEqual(record.contigs[0].reads[0].rt[0].padded_start, 590)
        self.assertEqual(record.contigs[0].reads[0].rt[0].padded_end, 607)
        self.assertEqual(record.contigs[0].reads[0].rt[0].date, "040217:110357")
        self.assertEqual(record.contigs[0].reads[0].rt[1].name, "BL060c3-LR5.g.ab1")
        self.assertEqual(
            record.contigs[0].reads[0].rt[1].tag_type, "matchElsewhereHighQual"
        )
        self.assertEqual(record.contigs[0].reads[0].rt[1].program, "phrap")
        self.assertEqual(record.contigs[0].reads[0].rt[1].padded_start, 617)
        self.assertEqual(record.contigs[0].reads[0].rt[1].padded_end, 631)
        self.assertEqual(record.contigs[0].reads[0].rt[1].date, "040217:110357")
        self.assertEqual(record.contigs[0].reads[0].rt[2].name, "BL060c3-LR5.g.ab1")
        self.assertEqual(
            record.contigs[0].reads[0].rt[2].tag_type, "matchElsewhereHighQual"
        )
        self.assertEqual(record.contigs[0].reads[0].rt[2].program, "phrap")
        self.assertEqual(record.contigs[0].reads[0].rt[2].padded_start, 617)
        self.assertEqual(record.contigs[0].reads[0].rt[2].padded_end, 631)
        self.assertEqual(record.contigs[0].reads[0].rt[2].date, "040217:110357")
        self.assertEqual(record.contigs[0].reads[0].rt[3].name, "BL060c3-LR5.g.ab1")
        self.assertEqual(
            record.contigs[0].reads[0].rt[3].tag_type, "matchElsewhereHighQual"
        )
        self.assertEqual(record.contigs[0].reads[0].rt[3].program, "phrap")
        self.assertEqual(record.contigs[0].reads[0].rt[3].padded_start, 617)
        self.assertEqual(record.contigs[0].reads[0].rt[3].padded_end, 631)
        self.assertEqual(record.contigs[0].reads[0].rt[3].date, "040217:110357")

        self.assertEqual(len(record.contigs[0].reads[0].wr), 1)
        self.assertEqual(record.contigs[0].reads[0].wr[0].name, "BL060c3-LR5.g.ab1")
        self.assertEqual(record.contigs[0].reads[0].wr[0].aligned, "unaligned")
        self.assertEqual(record.contigs[0].reads[0].wr[0].program, "phrap")
        self.assertEqual(record.contigs[0].reads[0].wr[0].date, "040217:110357")
        self.assertEqual(record.contigs[0].reads[1].rd.name, "BL060c3-LR0R.b.ab1")
        self.assertEqual(record.contigs[0].reads[1].rd.padded_bases, 856)
        self.assertEqual(record.contigs[0].reads[1].rd.info_items, 0)
        self.assertEqual(record.contigs[0].reads[1].rd.read_tags, 0)
        center = len(record.contigs[0].reads[1].rd.sequence) // 2
        self.assertEqual(record.contigs[0].reads[1].rd.sequence[:10], "aatacgGGAT")
        self.assertEqual(
            record.contigs[0].reads[1].rd.sequence[center - 5 : center + 5],
            "ACATCATCTG",
        )
        self.assertEqual(record.contigs[0].reads[1].rd.sequence[-10:], "cATCTAGtac")
        self.assertEqual(record.contigs[0].reads[1].qa.qual_clipping_start, 7)
        self.assertEqual(record.contigs[0].reads[1].qa.qual_clipping_end, 778)
        self.assertEqual(record.contigs[0].reads[1].qa.align_clipping_start, 1)
        self.assertEqual(record.contigs[0].reads[1].qa.align_clipping_end, 856)
        self.assertIsNone(record.contigs[0].reads[1].ds)
        self.assertIsNone(record.contigs[0].reads[1].rt)
        self.assertIsNone(record.contigs[0].reads[1].wr)

        self.assertEqual(len(record.contigs[1].reads), 14)
        self.assertEqual(record.contigs[1].name, "Contig2")
        self.assertEqual(record.contigs[1].nbases, 3296)
        self.assertEqual(record.contigs[1].nreads, 14)
        self.assertEqual(record.contigs[1].nsegments, 214)
        self.assertEqual(record.contigs[1].uorc, "U")
        center = len(record.contigs[1].sequence) // 2
        self.assertEqual(record.contigs[1].sequence[:10], "cacggatgat")
        self.assertEqual(
            record.contigs[1].sequence[center - 5 : center + 5], "TTTGAATATT"
        )
        self.assertEqual(record.contigs[1].sequence[-10:], "Atccttgtag")
        center = len(record.contigs[1].quality) // 2
        self.assertEqual(record.contigs[1].quality[:10], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(
            record.contigs[1].quality[center - 5 : center + 5],
            [90, 90, 90, 90, 90, 90, 90, 90, 90, 90],
        )
        self.assertEqual(
            record.contigs[1].quality[-10:], [24, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        )
        self.assertEqual(len(record.contigs[1].af), 14)
        self.assertEqual(record.contigs[1].af[7].name, "BL060-LR3R.b.ab1")
        self.assertEqual(record.contigs[1].af[7].coru, "C")
        self.assertEqual(record.contigs[1].af[7].padded_start, 1601)
        self.assertEqual(record.contigs[1].af[13].name, "BL060c2-LR0R.b.ab1")
        self.assertEqual(record.contigs[1].af[13].coru, "C")
        self.assertEqual(record.contigs[1].af[13].padded_start, 2445)
        self.assertEqual(len(record.contigs[1].bs), 214)
        self.assertEqual(record.contigs[1].bs[107].name, "BL060-c1-LR3R.b.ab1")
        self.assertEqual(record.contigs[1].bs[107].padded_start, 2286)
        self.assertEqual(record.contigs[1].bs[107].padded_end, 2292)
        self.assertEqual(record.contigs[1].bs[213].name, "BL060c2-LR0R.b.ab1")
        self.assertEqual(record.contigs[1].bs[213].padded_start, 3236)
        self.assertEqual(record.contigs[1].bs[213].padded_end, 3296)
        self.assertEqual(len(record.contigs[1].ct), 1)
        self.assertEqual(record.contigs[1].ct[0].name, "Contig2")
        self.assertEqual(record.contigs[1].ct[0].tag_type, "repeat")
        self.assertEqual(record.contigs[1].ct[0].program, "phrap")
        self.assertEqual(record.contigs[1].ct[0].padded_start, 42)
        self.assertEqual(record.contigs[1].ct[0].padded_end, 43)
        self.assertEqual(record.contigs[1].ct[0].date, "123456:765432")
        self.assertEqual(
            record.contigs[1].ct[0].info,
            ["This is the first line of comment for c2", "and this the second for c2"],
        )
        self.assertEqual(len(record.contigs[1].wa), 1)
        self.assertEqual(record.contigs[1].wa[0].tag_type, "phrap_params")
        self.assertEqual(record.contigs[1].wa[0].program, "phrap")
        self.assertEqual(record.contigs[1].wa[0].date, "040203:114710")
        self.assertEqual(
            record.contigs[1].wa[0].info,
            [
                "phrap 304_nuclsu.fasta.screen -new_ace -retain_duplicates",
                "phrap version 0.990329",
            ],
        )

        self.assertEqual(len(record.contigs[1].reads), 14)

        # Read 0
        self.assertEqual(record.contigs[1].reads[0].rd.name, "BL060-c1-LR12.g.ab1")
        self.assertEqual(record.contigs[1].reads[0].rd.padded_bases, 862)
        self.assertEqual(record.contigs[1].reads[0].rd.info_items, 0)
        self.assertEqual(record.contigs[1].reads[0].rd.read_tags, 0)
        center = len(record.contigs[1].reads[0].rd.sequence) // 2
        self.assertEqual(record.contigs[1].reads[0].rd.sequence[:10], "cacggatgat")
        self.assertEqual(
            record.contigs[1].reads[0].rd.sequence[center - 5 : center + 5],
            "GTTCTCGTTG",
        )
        self.assertEqual(record.contigs[1].reads[0].rd.sequence[-10:], "CGTTTACCcg")
        self.assertEqual(record.contigs[1].reads[0].qa.qual_clipping_start, 81)
        self.assertEqual(record.contigs[1].reads[0].qa.qual_clipping_end, 842)
        self.assertEqual(record.contigs[1].reads[0].qa.align_clipping_start, 1)
        self.assertEqual(record.contigs[1].reads[0].qa.align_clipping_end, 862)
        self.assertEqual(
            record.contigs[1].reads[0].ds.chromat_file, "BL060-c1-LR12.g.ab1"
        )
        self.assertEqual(
            record.contigs[1].reads[0].ds.phd_file, "BL060-c1-LR12.g.ab1.phd.1"
        )
        self.assertEqual(record.contigs[1].reads[0].ds.time, "Tue Feb  3 11:01:16 2004")
        self.assertEqual(record.contigs[1].reads[0].ds.chem, "term")
        self.assertEqual(record.contigs[1].reads[0].ds.dye, "big")
        self.assertEqual(record.contigs[1].reads[0].ds.template, "")
        self.assertEqual(record.contigs[1].reads[0].ds.direction, "")
        self.assertIsNone(record.contigs[1].reads[0].rt)
        self.assertIsNone(record.contigs[1].reads[0].wr)

        # Read 1
        self.assertEqual(record.contigs[1].reads[1].rd.name, "BL060-c1-LR11.g.ab1")
        self.assertEqual(record.contigs[1].reads[1].rd.padded_bases, 880)
        self.assertEqual(record.contigs[1].reads[1].rd.info_items, 0)
        self.assertEqual(record.contigs[1].reads[1].rd.read_tags, 0)
        center = len(record.contigs[1].reads[1].rd.sequence) // 2
        self.assertEqual(record.contigs[1].reads[1].rd.sequence[:10], "ctttctgacC")
        self.assertEqual(
            record.contigs[1].reads[1].rd.sequence[center - 5 : center + 5],
            "CTGTGGTTTC",
        )
        self.assertEqual(record.contigs[1].reads[1].rd.sequence[-10:], "cggagttacg")
        self.assertEqual(record.contigs[1].reads[1].qa.qual_clipping_start, 11)
        self.assertEqual(record.contigs[1].reads[1].qa.qual_clipping_end, 807)
        self.assertEqual(record.contigs[1].reads[1].qa.align_clipping_start, 8)
        self.assertEqual(record.contigs[1].reads[1].qa.align_clipping_end, 880)
        self.assertEqual(
            record.contigs[1].reads[1].ds.chromat_file, "BL060-c1-LR11.g.ab1"
        )
        self.assertEqual(
            record.contigs[1].reads[1].ds.phd_file, "BL060-c1-LR11.g.ab1.phd.1"
        )
        self.assertEqual(record.contigs[1].reads[1].ds.time, "Tue Feb  3 11:01:16 2004")
        self.assertEqual(record.contigs[1].reads[1].ds.chem, "term")
        self.assertEqual(record.contigs[1].reads[1].ds.dye, "big")
        self.assertEqual(record.contigs[1].reads[1].ds.template, "")
        self.assertEqual(record.contigs[1].reads[1].ds.direction, "")
        self.assertEqual(len(record.contigs[1].reads[1].rt), 0)
        self.assertIsNone(record.contigs[1].reads[1].wr)

        # Read 2
        self.assertEqual(record.contigs[1].reads[2].rd.name, "BL060-c1-LR9.g.ab1")
        self.assertEqual(record.contigs[1].reads[2].rd.padded_bases, 864)
        self.assertEqual(record.contigs[1].reads[2].rd.info_items, 0)
        self.assertEqual(record.contigs[1].reads[2].rd.read_tags, 0)
        center = len(record.contigs[1].reads[2].rd.sequence) // 2
        self.assertEqual(record.contigs[1].reads[2].rd.sequence[:10], "cacccaCTTT")
        self.assertEqual(
            record.contigs[1].reads[2].rd.sequence[center - 5 : center + 5],
            "ACCAAACATT",
        )
        self.assertEqual(record.contigs[1].reads[2].rd.sequence[-10:], "GGTAGCACgc")
        self.assertEqual(record.contigs[1].reads[2].qa.qual_clipping_start, 7)
        self.assertEqual(record.contigs[1].reads[2].qa.qual_clipping_end, 840)
        self.assertEqual(record.contigs[1].reads[2].qa.align_clipping_start, 4)
        self.assertEqual(record.contigs[1].reads[2].qa.align_clipping_end, 864)
        self.assertEqual(
            record.contigs[1].reads[2].ds.chromat_file, "BL060-c1-LR9.g.ab1"
        )
        self.assertEqual(
            record.contigs[1].reads[2].ds.phd_file, "BL060-c1-LR9.g.ab1.phd.1"
        )
        self.assertEqual(record.contigs[1].reads[2].ds.time, "Tue Feb  3 11:01:16 2004")
        self.assertEqual(record.contigs[1].reads[2].ds.chem, "term")
        self.assertEqual(record.contigs[1].reads[2].ds.dye, "big")
        self.assertEqual(record.contigs[1].reads[2].ds.template, "")
        self.assertEqual(record.contigs[1].reads[2].ds.direction, "")
        self.assertIsNone(record.contigs[1].reads[2].rt)
        self.assertIsNone(record.contigs[1].reads[2].wr)

        # Read 3
        self.assertEqual(record.contigs[1].reads[3].rd.name, "BL060-c1-LR17R.b.ab1")
        self.assertEqual(record.contigs[1].reads[3].rd.padded_bases, 863)
        self.assertEqual(record.contigs[1].reads[3].rd.info_items, 0)
        self.assertEqual(record.contigs[1].reads[3].rd.read_tags, 0)
        center = len(record.contigs[1].reads[3].rd.sequence) // 2
        self.assertEqual(record.contigs[1].reads[3].rd.sequence[:10], "ctaattggcc")
        self.assertEqual(
            record.contigs[1].reads[3].rd.sequence[center - 5 : center + 5],
            "GGAACCTTTC",
        )
        self.assertEqual(record.contigs[1].reads[3].rd.sequence[-10:], "CAACCTgact")
        self.assertEqual(record.contigs[1].reads[3].qa.qual_clipping_start, 63)
        self.assertEqual(record.contigs[1].reads[3].qa.qual_clipping_end, 857)
        self.assertEqual(record.contigs[1].reads[3].qa.align_clipping_start, 1)
        self.assertEqual(record.contigs[1].reads[3].qa.align_clipping_end, 861)
        self.assertEqual(
            record.contigs[1].reads[3].ds.chromat_file, "BL060-c1-LR17R.b.ab1"
        )
        self.assertEqual(
            record.contigs[1].reads[3].ds.phd_file, "BL060-c1-LR17R.b.ab1.phd.1"
        )
        self.assertEqual(record.contigs[1].reads[3].ds.time, "Tue Feb  3 11:01:16 2004")
        self.assertEqual(record.contigs[1].reads[3].ds.chem, "term")
        self.assertEqual(record.contigs[1].reads[3].ds.dye, "big")
        self.assertEqual(record.contigs[1].reads[3].ds.template, "")
        self.assertEqual(record.contigs[1].reads[3].ds.direction, "")
        self.assertEqual(record.contigs[1].reads[3].rt, [])
        self.assertIsNone(record.contigs[1].reads[3].wr)

        # Read 4
        self.assertEqual(record.contigs[1].reads[4].rd.name, "BL060-LR8.5.g.ab1")
        self.assertEqual(record.contigs[1].reads[4].rd.padded_bases, 877)
        self.assertEqual(record.contigs[1].reads[4].rd.info_items, 0)
        self.assertEqual(record.contigs[1].reads[4].rd.read_tags, 0)
        center = len(record.contigs[1].reads[4].rd.sequence) // 2
        self.assertEqual(record.contigs[1].reads[4].rd.sequence[:10], "tgCTGCGGTT")
        self.assertEqual(
            record.contigs[1].reads[4].rd.sequence[center - 5 : center + 5],
            "GGCAGTTTCA",
        )
        self.assertEqual(record.contigs[1].reads[4].rd.sequence[-10:], "tactcataaa")
        self.assertEqual(record.contigs[1].reads[4].qa.qual_clipping_start, 13)
        self.assertEqual(record.contigs[1].reads[4].qa.qual_clipping_end, 729)
        self.assertEqual(record.contigs[1].reads[4].qa.align_clipping_start, 1)
        self.assertEqual(record.contigs[1].reads[4].qa.align_clipping_end, 877)
        self.assertEqual(
            record.contigs[1].reads[4].ds.chromat_file, "BL060-LR8.5.g.ab1"
        )
        self.assertEqual(
            record.contigs[1].reads[4].ds.phd_file, "BL060-LR8.5.g.ab1.phd.1"
        )
        self.assertEqual(record.contigs[1].reads[4].ds.time, "Fri Nov 14 09:46:03 2003")
        self.assertEqual(record.contigs[1].reads[4].ds.chem, "term")
        self.assertEqual(record.contigs[1].reads[4].ds.dye, "big")
        self.assertEqual(record.contigs[1].reads[4].ds.template, "")
        self.assertEqual(record.contigs[1].reads[4].ds.direction, "")
        self.assertIsNone(record.contigs[1].reads[4].rt)
        self.assertIsNone(record.contigs[1].reads[4].wr)

        # Read 5
        self.assertEqual(record.contigs[1].reads[5].rd.name, "BL060-LR3R.b.ab1")
        self.assertEqual(record.contigs[1].reads[5].rd.padded_bases, 874)
        self.assertEqual(record.contigs[1].reads[5].rd.info_items, 0)
        self.assertEqual(record.contigs[1].reads[5].rd.read_tags, 0)
        center = len(record.contigs[1].reads[5].rd.sequence) // 2
        self.assertEqual(record.contigs[1].reads[5].rd.sequence[:10], "ctCTTAGGAT")
        self.assertEqual(
            record.contigs[1].reads[5].rd.sequence[center - 5 : center + 5],
            "AACTCACATT",
        )
        self.assertEqual(record.contigs[1].reads[5].rd.sequence[-10:], "*CACCCAAac")
        self.assertEqual(record.contigs[1].reads[5].qa.qual_clipping_start, 65)
        self.assertEqual(record.contigs[1].reads[5].qa.qual_clipping_end, 874)
        self.assertEqual(record.contigs[1].reads[5].qa.align_clipping_start, 1)
        self.assertEqual(record.contigs[1].reads[5].qa.align_clipping_end, 874)
        self.assertEqual(record.contigs[1].reads[5].ds.chromat_file, "BL060-LR3R.b.ab1")
        self.assertEqual(
            record.contigs[1].reads[5].ds.phd_file, "BL060-LR3R.b.ab1.phd.1"
        )
        self.assertEqual(record.contigs[1].reads[5].ds.time, "Fri Nov 14 09:46:03 2003")
        self.assertEqual(record.contigs[1].reads[5].ds.chem, "term")
        self.assertEqual(record.contigs[1].reads[5].ds.dye, "big")
        self.assertEqual(record.contigs[1].reads[5].ds.template, "")
        self.assertEqual(record.contigs[1].reads[5].ds.direction, "")
        self.assertIsNone(record.contigs[1].reads[5].rt)
        self.assertIsNone(record.contigs[1].reads[5].wr)

        # Read 6
        self.assertEqual(record.contigs[1].reads[6].rd.name, "BL060-c1-LR3R.b.ab1")
        self.assertEqual(record.contigs[1].reads[6].rd.padded_bases, 864)
        self.assertEqual(record.contigs[1].reads[6].rd.info_items, 0)
        self.assertEqual(record.contigs[1].reads[6].rd.read_tags, 0)
        center = len(record.contigs[1].reads[6].rd.sequence) // 2
        self.assertEqual(record.contigs[1].reads[6].rd.sequence[:10], "CCaTGTCCAA")
        self.assertEqual(
            record.contigs[1].reads[6].rd.sequence[center - 5 : center + 5],
            "AAGGGTT*CA",
        )
        self.assertEqual(record.contigs[1].reads[6].rd.sequence[-10:], "ACACTCGCga")
        self.assertEqual(record.contigs[1].reads[6].qa.qual_clipping_start, 73)
        self.assertEqual(record.contigs[1].reads[6].qa.qual_clipping_end, 862)
        self.assertEqual(record.contigs[1].reads[6].qa.align_clipping_start, 1)
        self.assertEqual(record.contigs[1].reads[6].qa.align_clipping_end, 863)
        self.assertEqual(
            record.contigs[1].reads[6].ds.chromat_file, "BL060-c1-LR3R.b.ab1"
        )
        self.assertEqual(
            record.contigs[1].reads[6].ds.phd_file, "BL060-c1-LR3R.b.ab1.phd.1"
        )
        self.assertEqual(record.contigs[1].reads[6].ds.time, "Tue Feb  3 11:01:16 2004")
        self.assertEqual(record.contigs[1].reads[6].ds.chem, "term")
        self.assertEqual(record.contigs[1].reads[6].ds.dye, "big")
        self.assertEqual(record.contigs[1].reads[6].ds.template, "")
        self.assertEqual(record.contigs[1].reads[6].ds.direction, "")
        self.assertIsNone(record.contigs[1].reads[6].rt)
        self.assertIsNone(record.contigs[1].reads[6].wr)

        # Read 7
        self.assertEqual(record.contigs[1].reads[7].rd.name, "BL060-LR3R.b.ab1")
        self.assertEqual(record.contigs[1].reads[7].rd.padded_bases, 857)
        self.assertEqual(record.contigs[1].reads[7].rd.info_items, 0)
        self.assertEqual(record.contigs[1].reads[7].rd.read_tags, 0)
        center = len(record.contigs[1].reads[7].rd.sequence) // 2
        self.assertEqual(record.contigs[1].reads[7].rd.sequence[:10], "agaaagagga")
        self.assertEqual(
            record.contigs[1].reads[7].rd.sequence[center - 5 : center + 5],
            "nnnannnnnn",
        )
        self.assertEqual(record.contigs[1].reads[7].rd.sequence[-10:], "gtctttgctc")
        self.assertEqual(record.contigs[1].reads[7].qa.qual_clipping_start, 548)
        self.assertEqual(record.contigs[1].reads[7].qa.qual_clipping_end, 847)
        self.assertEqual(record.contigs[1].reads[7].qa.align_clipping_start, 442)
        self.assertEqual(record.contigs[1].reads[7].qa.align_clipping_end, 854)
        self.assertEqual(record.contigs[1].reads[7].ds.chromat_file, "BL060-LR3R.b.ab1")
        self.assertEqual(
            record.contigs[1].reads[7].ds.phd_file, "BL060-LR3R.b.ab1.phd.1"
        )
        self.assertEqual(record.contigs[1].reads[7].ds.time, "Fri Jan 16 09:01:10 2004")
        self.assertEqual(record.contigs[1].reads[7].ds.chem, "term")
        self.assertEqual(record.contigs[1].reads[7].ds.dye, "big")
        self.assertEqual(record.contigs[1].reads[7].ds.template, "")
        self.assertEqual(record.contigs[1].reads[7].ds.direction, "")
        self.assertIsNone(record.contigs[1].reads[7].rt)
        self.assertIsNone(record.contigs[1].reads[7].wr)

        # Read 8
        self.assertEqual(record.contigs[1].reads[8].rd.name, "BL060-c1-LR7.g.ab1")
        self.assertEqual(record.contigs[1].reads[8].rd.padded_bases, 878)
        self.assertEqual(record.contigs[1].reads[8].rd.info_items, 0)
        self.assertEqual(record.contigs[1].reads[8].rd.read_tags, 0)
        center = len(record.contigs[1].reads[8].rd.sequence) // 2
        self.assertEqual(record.contigs[1].reads[8].rd.sequence[:10], "agTttc*ctc")
        self.assertEqual(
            record.contigs[1].reads[8].rd.sequence[center - 5 : center + 5],
            "TCATAAAACT",
        )
        self.assertEqual(record.contigs[1].reads[8].rd.sequence[-10:], "xxxxxxxxxx")
        self.assertEqual(record.contigs[1].reads[8].qa.qual_clipping_start, 20)
        self.assertEqual(record.contigs[1].reads[8].qa.qual_clipping_end, 798)
        self.assertEqual(record.contigs[1].reads[8].qa.align_clipping_start, 1)
        self.assertEqual(record.contigs[1].reads[8].qa.align_clipping_end, 798)
        self.assertEqual(
            record.contigs[1].reads[8].ds.chromat_file, "BL060-c1-LR7.g.ab1"
        )
        self.assertEqual(
            record.contigs[1].reads[8].ds.phd_file, "BL060-c1-LR7.g.ab1.phd.1"
        )
        self.assertEqual(record.contigs[1].reads[8].ds.time, "Tue Feb  3 11:01:16 2004")
        self.assertEqual(record.contigs[1].reads[8].ds.chem, "term")
        self.assertEqual(record.contigs[1].reads[8].ds.dye, "big")
        self.assertEqual(record.contigs[1].reads[8].ds.template, "")
        self.assertEqual(record.contigs[1].reads[8].ds.direction, "")
        self.assertIsNone(record.contigs[1].reads[8].rt)
        self.assertIsNone(record.contigs[1].reads[8].wr)

        # Read 9
        self.assertEqual(record.contigs[1].reads[9].rd.name, "BL060-LR7.g.ab1")
        self.assertEqual(record.contigs[1].reads[9].rd.padded_bases, 880)
        self.assertEqual(record.contigs[1].reads[9].rd.info_items, 0)
        self.assertEqual(record.contigs[1].reads[9].rd.read_tags, 0)
        center = len(record.contigs[1].reads[9].rd.sequence) // 2
        self.assertEqual(record.contigs[1].reads[9].rd.sequence[:10], "ggctaCGCCc")
        self.assertEqual(
            record.contigs[1].reads[9].rd.sequence[center - 5 : center + 5],
            "ATTGAGTTTC",
        )
        self.assertEqual(record.contigs[1].reads[9].rd.sequence[-10:], "tggcgttgcg")
        self.assertEqual(record.contigs[1].reads[9].qa.qual_clipping_start, 14)
        self.assertEqual(record.contigs[1].reads[9].qa.qual_clipping_end, 765)
        self.assertEqual(record.contigs[1].reads[9].qa.align_clipping_start, 4)
        self.assertEqual(record.contigs[1].reads[9].qa.align_clipping_end, 765)
        self.assertEqual(record.contigs[1].reads[9].ds.chromat_file, "BL060-LR7.g.ab1")
        self.assertEqual(
            record.contigs[1].reads[9].ds.phd_file, "BL060-LR7.g.ab1.phd.1"
        )
        self.assertEqual(record.contigs[1].reads[9].ds.time, "Fri Nov 14 09:46:03 2003")
        self.assertEqual(record.contigs[1].reads[9].ds.chem, "term")
        self.assertEqual(record.contigs[1].reads[9].ds.dye, "big")
        self.assertEqual(record.contigs[1].reads[9].ds.template, "")
        self.assertEqual(record.contigs[1].reads[9].ds.direction, "")
        self.assertIsNone(record.contigs[1].reads[9].rt)
        self.assertIsNone(record.contigs[1].reads[9].wr)

        # Read 10
        self.assertEqual(record.contigs[1].reads[10].rd.name, "BL060c5-LR5.g.ab1")
        self.assertEqual(record.contigs[1].reads[10].rd.padded_bases, 871)
        self.assertEqual(record.contigs[1].reads[10].rd.info_items, 0)
        self.assertEqual(record.contigs[1].reads[10].rd.read_tags, 0)
        center = len(record.contigs[1].reads[10].rd.sequence) // 2
        self.assertEqual(record.contigs[1].reads[10].rd.sequence[:10], "ggtTCGATTA")
        self.assertEqual(
            record.contigs[1].reads[10].rd.sequence[center - 5 : center + 5],
            "ACCAATTGAC",
        )
        self.assertEqual(record.contigs[1].reads[10].rd.sequence[-10:], "ACCACCCatt")
        self.assertEqual(record.contigs[1].reads[10].qa.qual_clipping_start, 12)
        self.assertEqual(record.contigs[1].reads[10].qa.qual_clipping_end, 767)
        self.assertEqual(record.contigs[1].reads[10].qa.align_clipping_start, 1)
        self.assertEqual(record.contigs[1].reads[10].qa.align_clipping_end, 871)
        self.assertEqual(
            record.contigs[1].reads[10].ds.chromat_file, "BL060c5-LR5.g.ab1"
        )
        self.assertEqual(
            record.contigs[1].reads[10].ds.phd_file, "BL060c5-LR5.g.ab1.phd.1"
        )
        self.assertEqual(
            record.contigs[1].reads[10].ds.time, "Fri Nov 14 09:46:03 2003"
        )
        self.assertEqual(record.contigs[1].reads[10].ds.chem, "term")
        self.assertEqual(record.contigs[1].reads[10].ds.dye, "big")
        self.assertEqual(record.contigs[1].reads[10].ds.template, "")
        self.assertEqual(record.contigs[1].reads[10].ds.direction, "")
        self.assertIsNone(record.contigs[1].reads[10].rt)
        self.assertIsNone(record.contigs[1].reads[10].wr)

        # Read 11
        self.assertEqual(record.contigs[1].reads[11].rd.name, "BL060c2-LR5.g.ab1")
        self.assertEqual(record.contigs[1].reads[11].rd.padded_bases, 839)
        self.assertEqual(record.contigs[1].reads[11].rd.info_items, 0)
        self.assertEqual(record.contigs[1].reads[11].rd.read_tags, 0)
        center = len(record.contigs[1].reads[11].rd.sequence) // 2
        self.assertEqual(record.contigs[1].reads[11].rd.sequence[:10], "ggttcatatg")
        self.assertEqual(
            record.contigs[1].reads[11].rd.sequence[center - 5 : center + 5],
            "TAAAATCAGT",
        )
        self.assertEqual(record.contigs[1].reads[11].rd.sequence[-10:], "TCTTGCaata")
        self.assertEqual(record.contigs[1].reads[11].qa.qual_clipping_start, 11)
        self.assertEqual(record.contigs[1].reads[11].qa.qual_clipping_end, 757)
        self.assertEqual(record.contigs[1].reads[11].qa.align_clipping_start, 10)
        self.assertEqual(record.contigs[1].reads[11].qa.align_clipping_end, 835)
        self.assertIsNone(record.contigs[1].reads[11].ds)
        self.assertEqual(len(record.contigs[1].reads[11].rt), 1)
        self.assertEqual(record.contigs[1].reads[11].rt[0].name, "BL060c2-LR5.g.ab1")
        self.assertEqual(
            record.contigs[1].reads[11].rt[0].tag_type, "matchElsewhereHighQual"
        )
        self.assertEqual(record.contigs[1].reads[11].rt[0].program, "phrap")
        self.assertEqual(record.contigs[1].reads[11].rt[0].padded_start, 617)
        self.assertEqual(record.contigs[1].reads[11].rt[0].padded_end, 631)
        self.assertEqual(record.contigs[1].reads[11].rt[0].date, "040217:110357")
        self.assertIsNone(record.contigs[1].reads[11].wr)

        # Read 12
        self.assertEqual(record.contigs[1].reads[12].rd.name, "BL060c5-LR0R.b.ab1")
        self.assertEqual(record.contigs[1].reads[12].rd.padded_bases, 855)
        self.assertEqual(record.contigs[1].reads[12].rd.info_items, 0)
        self.assertEqual(record.contigs[1].reads[12].rd.read_tags, 0)
        center = len(record.contigs[1].reads[12].rd.sequence) // 2
        self.assertEqual(record.contigs[1].reads[12].rd.sequence[:10], "cACTCGCGTA")
        self.assertEqual(
            record.contigs[1].reads[12].rd.sequence[center - 5 : center + 5],
            "CTCGTAAAAT",
        )
        self.assertEqual(record.contigs[1].reads[12].rd.sequence[-10:], "aacccctgca")
        self.assertEqual(record.contigs[1].reads[12].qa.qual_clipping_start, 94)
        self.assertEqual(record.contigs[1].reads[12].qa.qual_clipping_end, 835)
        self.assertEqual(record.contigs[1].reads[12].qa.align_clipping_start, 1)
        self.assertEqual(record.contigs[1].reads[12].qa.align_clipping_end, 847)
        self.assertEqual(
            record.contigs[1].reads[12].ds.chromat_file, "BL060c5-LR0R.b.ab1"
        )
        self.assertEqual(
            record.contigs[1].reads[12].ds.phd_file, "BL060c5-LR0R.b.ab1.phd.1"
        )
        self.assertEqual(
            record.contigs[1].reads[12].ds.time, "Wed Nov 12 08:16:30 2003"
        )
        self.assertEqual(record.contigs[1].reads[12].ds.chem, "term")
        self.assertEqual(record.contigs[1].reads[12].ds.dye, "big")
        self.assertEqual(record.contigs[1].reads[12].ds.template, "")
        self.assertEqual(record.contigs[1].reads[12].ds.direction, "")
        self.assertEqual(len(record.contigs[1].reads[12].rt), 1)
        self.assertEqual(record.contigs[1].reads[12].rt[0].name, "BL060c5-LR0R.b.ab1")
        self.assertEqual(
            record.contigs[1].reads[12].rt[0].tag_type, "matchElsewhereHighQual"
        )
        self.assertEqual(record.contigs[1].reads[12].rt[0].program, "phrap")
        self.assertEqual(record.contigs[1].reads[12].rt[0].padded_start, 617)
        self.assertEqual(record.contigs[1].reads[12].rt[0].padded_end, 631)
        self.assertEqual(record.contigs[1].reads[12].rt[0].date, "040217:110357")
        self.assertIsNone(record.contigs[1].reads[12].wr)

        # Read 13
        self.assertEqual(record.contigs[1].reads[13].rd.name, "BL060c2-LR0R.b.ab1")
        self.assertEqual(record.contigs[1].reads[13].rd.padded_bases, 852)
        self.assertEqual(record.contigs[1].reads[13].rd.info_items, 0)
        self.assertEqual(record.contigs[1].reads[13].rd.read_tags, 0)
        center = len(record.contigs[1].reads[13].rd.sequence) // 2
        self.assertEqual(record.contigs[1].reads[13].rd.sequence[:10], "cgCGTa*tTG")
        self.assertEqual(
            record.contigs[1].reads[13].rd.sequence[center - 5 : center + 5],
            "GTAAAATATT",
        )
        self.assertEqual(record.contigs[1].reads[13].rd.sequence[-10:], "Atccttgtag")
        self.assertEqual(record.contigs[1].reads[13].qa.qual_clipping_start, 33)
        self.assertEqual(record.contigs[1].reads[13].qa.qual_clipping_end, 831)
        self.assertEqual(record.contigs[1].reads[13].qa.align_clipping_start, 1)
        self.assertEqual(record.contigs[1].reads[13].qa.align_clipping_end, 852)
        self.assertEqual(
            record.contigs[1].reads[13].ds.chromat_file, "BL060c2-LR0R.b.ab1"
        )
        self.assertEqual(
            record.contigs[1].reads[13].ds.phd_file, "BL060c2-LR0R.b.ab1.phd.1"
        )
        self.assertEqual(
            record.contigs[1].reads[13].ds.time, "Wed Nov 12 08:16:29 2003"
        )
        self.assertEqual(record.contigs[1].reads[13].ds.chem, "term")
        self.assertEqual(record.contigs[1].reads[13].ds.dye, "big")
        self.assertEqual(record.contigs[1].reads[13].ds.template, "")
        self.assertEqual(record.contigs[1].reads[13].ds.direction, "")
        self.assertEqual(record.contigs[1].reads[13].rt, [])
        self.assertEqual(len(record.contigs[1].reads[13].wr), 1)
        self.assertEqual(record.contigs[1].reads[13].wr[0].name, "BL060c2-LR0R.b.ab1")
        self.assertEqual(record.contigs[1].reads[13].wr[0].aligned, "unaligned")
        self.assertEqual(record.contigs[1].reads[13].wr[0].program, "phrap")
        self.assertEqual(record.contigs[1].reads[13].wr[0].date, "040217:110357")

    def test_check_record_parser(self):
        """Test to check that contig parser parses each contig into a contig."""
        contigs = Ace.parse(self.handle)

        # First contig
        contig = next(contigs)
        self.assertEqual(len(contig.reads), 2)
        self.assertEqual(contig.name, "Contig1")
        self.assertEqual(contig.nbases, 856)
        self.assertEqual(contig.nreads, 2)
        self.assertEqual(contig.nsegments, 31)
        self.assertEqual(contig.uorc, "U")
        center = len(contig.sequence) // 2
        self.assertEqual(contig.sequence[:10], "aatacgGGAT")
        self.assertEqual(contig.sequence[center - 5 : center + 5], "ACATCATCTG")
        self.assertEqual(contig.sequence[-10:], "cATCTAGtac")
        center = len(contig.quality) // 2
        self.assertEqual(contig.quality[:10], [0, 0, 0, 0, 0, 0, 22, 23, 25, 28])
        self.assertEqual(
            contig.quality[center - 5 : center + 5],
            [90, 90, 90, 90, 90, 90, 90, 90, 90, 90],
        )
        self.assertEqual(contig.quality[-10:], [15, 22, 30, 24, 28, 22, 21, 15, 19, 0])
        self.assertEqual(len(contig.af), 2)
        self.assertEqual(contig.af[1].name, "BL060c3-LR0R.b.ab1")
        self.assertEqual(contig.af[1].coru, "U")
        self.assertEqual(contig.af[1].padded_start, 1)
        self.assertEqual(len(contig.bs), 31)
        self.assertEqual(contig.bs[15].name, "BL060c3-LR5.g.ab1")
        self.assertEqual(contig.bs[15].padded_start, 434)
        self.assertEqual(contig.bs[15].padded_end, 438)
        self.assertEqual(contig.bs[30].name, "BL060c3-LR0R.b.ab1")
        self.assertEqual(contig.bs[30].padded_start, 823)
        self.assertEqual(contig.bs[30].padded_end, 856)
        self.assertIsNone(contig.ct)
        self.assertIsNone(contig.wa)
        self.assertEqual(len(contig.reads), 2)
        self.assertEqual(contig.reads[0].rd.name, "BL060c3-LR5.g.ab1")
        self.assertEqual(contig.reads[0].rd.padded_bases, 868)
        self.assertEqual(contig.reads[0].rd.info_items, 0)
        self.assertEqual(contig.reads[0].rd.read_tags, 0)
        center = len(contig.reads[0].rd.sequence) // 2
        self.assertEqual(contig.reads[0].rd.sequence[:10], "tagcgaggaa")
        self.assertEqual(
            contig.reads[0].rd.sequence[center - 5 : center + 5], "CCGAGGCCAA"
        )
        self.assertEqual(contig.reads[0].rd.sequence[-10:], "gaaccatcag")
        self.assertEqual(contig.reads[0].qa.qual_clipping_start, 80)
        self.assertEqual(contig.reads[0].qa.qual_clipping_end, 853)
        self.assertEqual(contig.reads[0].qa.align_clipping_start, 22)
        self.assertEqual(contig.reads[0].qa.align_clipping_end, 856)
        self.assertIsNone(contig.reads[0].ds)
        self.assertEqual(len(contig.reads[0].rt), 2)
        self.assertEqual(contig.reads[0].rt[0].name, "BL060c3-LR5.g.ab1")
        self.assertEqual(contig.reads[0].rt[0].tag_type, "matchElsewhereHighQual")
        self.assertEqual(contig.reads[0].rt[0].program, "phrap")
        self.assertEqual(contig.reads[0].rt[0].padded_start, 590)
        self.assertEqual(contig.reads[0].rt[0].padded_end, 607)
        self.assertEqual(contig.reads[0].rt[0].date, "040217:110357")
        self.assertEqual(contig.reads[0].rt[1].name, "BL060c3-LR5.g.ab1")
        self.assertEqual(contig.reads[0].rt[1].tag_type, "matchElsewhereHighQual")
        self.assertEqual(contig.reads[0].rt[1].program, "phrap")
        self.assertEqual(contig.reads[0].rt[1].padded_start, 617)
        self.assertEqual(contig.reads[0].rt[1].padded_end, 631)
        self.assertEqual(contig.reads[0].rt[1].date, "040217:110357")

        self.assertEqual(len(contig.reads[0].wr), 1)
        self.assertEqual(contig.reads[0].wr[0].name, "BL060c3-LR5.g.ab1")
        self.assertEqual(contig.reads[0].wr[0].aligned, "unaligned")
        self.assertEqual(contig.reads[0].wr[0].program, "phrap")
        self.assertEqual(contig.reads[0].wr[0].date, "040217:110357")

        self.assertEqual(contig.reads[1].rd.name, "BL060c3-LR0R.b.ab1")
        self.assertEqual(contig.reads[1].rd.padded_bases, 856)
        self.assertEqual(contig.reads[1].rd.info_items, 0)
        self.assertEqual(contig.reads[1].rd.read_tags, 0)
        center = len(contig.reads[1].rd.sequence) // 2
        self.assertEqual(contig.reads[1].rd.sequence[:10], "aatacgGGAT")
        self.assertEqual(
            contig.reads[1].rd.sequence[center - 5 : center + 5], "ACATCATCTG"
        )
        self.assertEqual(contig.reads[1].rd.sequence[-10:], "cATCTAGtac")
        self.assertEqual(contig.reads[1].qa.qual_clipping_start, 7)
        self.assertEqual(contig.reads[1].qa.qual_clipping_end, 778)
        self.assertEqual(contig.reads[1].qa.align_clipping_start, 1)
        self.assertEqual(contig.reads[1].qa.align_clipping_end, 856)
        self.assertIsNone(contig.reads[1].ds)
        self.assertIsNone(contig.reads[1].rt)
        self.assertIsNone(contig.reads[1].wr)

        # Second contig
        contig = next(contigs)
        self.assertEqual(len(contig.reads), 14)
        self.assertEqual(contig.name, "Contig2")
        self.assertEqual(contig.nbases, 3296)
        self.assertEqual(contig.nreads, 14)
        self.assertEqual(contig.nsegments, 214)
        self.assertEqual(contig.uorc, "U")
        center = len(contig.sequence) // 2
        self.assertEqual(contig.sequence[:10], "cacggatgat")
        self.assertEqual(contig.sequence[center - 5 : center + 5], "TTTGAATATT")
        self.assertEqual(contig.sequence[-10:], "Atccttgtag")
        center = len(contig.quality) // 2
        self.assertEqual(contig.quality[:10], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(
            contig.quality[center - 5 : center + 5],
            [90, 90, 90, 90, 90, 90, 90, 90, 90, 90],
        )
        self.assertEqual(contig.quality[-10:], [24, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(len(contig.af), 14)
        self.assertEqual(contig.af[7].name, "BL060-LR3R.b.ab1")
        self.assertEqual(contig.af[7].coru, "C")
        self.assertEqual(contig.af[7].padded_start, 1601)
        self.assertEqual(contig.af[13].name, "BL060c2-LR0R.b.ab1")
        self.assertEqual(contig.af[13].coru, "C")
        self.assertEqual(contig.af[13].padded_start, 2445)
        self.assertEqual(len(contig.bs), 214)
        self.assertEqual(contig.bs[107].name, "BL060-c1-LR3R.b.ab1")
        self.assertEqual(contig.bs[107].padded_start, 2286)
        self.assertEqual(contig.bs[107].padded_end, 2292)
        self.assertEqual(contig.bs[213].name, "BL060c2-LR0R.b.ab1")
        self.assertEqual(contig.bs[213].padded_start, 3236)
        self.assertEqual(contig.bs[213].padded_end, 3296)
        self.assertEqual(len(contig.ct), 3)
        self.assertEqual(contig.ct[0].name, "Contig2")
        self.assertEqual(contig.ct[0].tag_type, "repeat")
        self.assertEqual(contig.ct[0].program, "phrap")
        self.assertEqual(contig.ct[0].padded_start, 42)
        self.assertEqual(contig.ct[0].padded_end, 43)
        self.assertEqual(contig.ct[0].date, "123456:765432")
        self.assertEqual(
            contig.ct[0].info,
            ["This is the first line of comment for c2", "and this the second for c2"],
        )
        self.assertEqual(contig.ct[1].name, "unrelated_Contig")
        self.assertEqual(contig.ct[1].tag_type, "repeat")
        self.assertEqual(contig.ct[1].program, "phrap")
        self.assertEqual(contig.ct[1].padded_start, 1142)
        self.assertEqual(contig.ct[1].padded_end, 143)
        self.assertEqual(contig.ct[1].date, "122226:722232")
        self.assertEqual(
            contig.ct[1].info,
            [
                "This is the first line of comment for the unrelated ct tag",
                "and this the second",
            ],
        )

        self.assertEqual(contig.ct[2].name, "Contig1")
        self.assertEqual(contig.ct[2].tag_type, "repeat")
        self.assertEqual(contig.ct[2].program, "phrap")
        self.assertEqual(contig.ct[2].padded_start, 52)
        self.assertEqual(contig.ct[2].padded_end, 53)
        self.assertEqual(contig.ct[2].date, "555456:555432")
        self.assertEqual(
            contig.ct[2].info,
            ["This is the first line of comment for c1", "and this the second for c1"],
        )

        self.assertEqual(len(contig.wa), 1)
        self.assertEqual(contig.wa[0].tag_type, "phrap_params")
        self.assertEqual(contig.wa[0].program, "phrap")
        self.assertEqual(contig.wa[0].date, "040203:114710")
        self.assertEqual(
            contig.wa[0].info,
            [
                "phrap 304_nuclsu.fasta.screen -new_ace -retain_duplicates",
                "phrap version 0.990329",
            ],
        )

        self.assertEqual(len(contig.reads), 14)

        # Read 0
        self.assertEqual(contig.reads[0].rd.name, "BL060-c1-LR12.g.ab1")
        self.assertEqual(contig.reads[0].rd.padded_bases, 862)
        self.assertEqual(contig.reads[0].rd.info_items, 0)
        self.assertEqual(contig.reads[0].rd.read_tags, 0)
        center = len(contig.reads[0].rd.sequence) // 2
        self.assertEqual(contig.reads[0].rd.sequence[:10], "cacggatgat")
        self.assertEqual(
            contig.reads[0].rd.sequence[center - 5 : center + 5], "GTTCTCGTTG"
        )
        self.assertEqual(contig.reads[0].rd.sequence[-10:], "CGTTTACCcg")
        self.assertEqual(contig.reads[0].qa.qual_clipping_start, 81)
        self.assertEqual(contig.reads[0].qa.qual_clipping_end, 842)
        self.assertEqual(contig.reads[0].qa.align_clipping_start, 1)
        self.assertEqual(contig.reads[0].qa.align_clipping_end, 862)
        self.assertEqual(contig.reads[0].ds.chromat_file, "BL060-c1-LR12.g.ab1")
        self.assertEqual(contig.reads[0].ds.phd_file, "BL060-c1-LR12.g.ab1.phd.1")
        self.assertEqual(contig.reads[0].ds.time, "Tue Feb  3 11:01:16 2004")
        self.assertEqual(contig.reads[0].ds.chem, "term")
        self.assertEqual(contig.reads[0].ds.dye, "big")
        self.assertEqual(contig.reads[0].ds.template, "")
        self.assertEqual(contig.reads[0].ds.direction, "")
        self.assertIsNone(contig.reads[0].rt)
        self.assertIsNone(contig.reads[0].wr)

        # Read 1
        self.assertEqual(contig.reads[1].rd.name, "BL060-c1-LR11.g.ab1")
        self.assertEqual(contig.reads[1].rd.padded_bases, 880)
        self.assertEqual(contig.reads[1].rd.info_items, 0)
        self.assertEqual(contig.reads[1].rd.read_tags, 0)
        center = len(contig.reads[1].rd.sequence) // 2
        self.assertEqual(contig.reads[1].rd.sequence[:10], "ctttctgacC")
        self.assertEqual(
            contig.reads[1].rd.sequence[center - 5 : center + 5], "CTGTGGTTTC"
        )
        self.assertEqual(contig.reads[1].rd.sequence[-10:], "cggagttacg")
        self.assertEqual(contig.reads[1].qa.qual_clipping_start, 11)
        self.assertEqual(contig.reads[1].qa.qual_clipping_end, 807)
        self.assertEqual(contig.reads[1].qa.align_clipping_start, 8)
        self.assertEqual(contig.reads[1].qa.align_clipping_end, 880)
        self.assertEqual(contig.reads[1].ds.chromat_file, "BL060-c1-LR11.g.ab1")
        self.assertEqual(contig.reads[1].ds.phd_file, "BL060-c1-LR11.g.ab1.phd.1")
        self.assertEqual(contig.reads[1].ds.time, "Tue Feb  3 11:01:16 2004")
        self.assertEqual(contig.reads[1].ds.chem, "term")
        self.assertEqual(contig.reads[1].ds.dye, "big")
        self.assertEqual(contig.reads[1].ds.template, "")
        self.assertEqual(contig.reads[1].ds.direction, "")
        self.assertEqual(len(contig.reads[1].rt), 1)
        self.assertEqual(contig.reads[1].rt[0].name, "BL060c3-LR5.g.ab1")
        self.assertEqual(contig.reads[1].rt[0].tag_type, "matchElsewhereHighQual")
        self.assertEqual(contig.reads[1].rt[0].program, "phrap")
        self.assertEqual(contig.reads[1].rt[0].padded_start, 617)
        self.assertEqual(contig.reads[1].rt[0].padded_end, 631)
        self.assertEqual(contig.reads[1].rt[0].date, "040217:110357")
        self.assertIsNone(contig.reads[1].wr)

        # Read 2
        self.assertEqual(contig.reads[2].rd.name, "BL060-c1-LR9.g.ab1")
        self.assertEqual(contig.reads[2].rd.padded_bases, 864)
        self.assertEqual(contig.reads[2].rd.info_items, 0)
        self.assertEqual(contig.reads[2].rd.read_tags, 0)
        center = len(contig.reads[2].rd.sequence) // 2
        self.assertEqual(contig.reads[2].rd.sequence[:10], "cacccaCTTT")
        self.assertEqual(
            contig.reads[2].rd.sequence[center - 5 : center + 5], "ACCAAACATT"
        )
        self.assertEqual(contig.reads[2].rd.sequence[-10:], "GGTAGCACgc")
        self.assertEqual(contig.reads[2].qa.qual_clipping_start, 7)
        self.assertEqual(contig.reads[2].qa.qual_clipping_end, 840)
        self.assertEqual(contig.reads[2].qa.align_clipping_start, 4)
        self.assertEqual(contig.reads[2].qa.align_clipping_end, 864)
        self.assertEqual(contig.reads[2].ds.chromat_file, "BL060-c1-LR9.g.ab1")
        self.assertEqual(contig.reads[2].ds.phd_file, "BL060-c1-LR9.g.ab1.phd.1")
        self.assertEqual(contig.reads[2].ds.time, "Tue Feb  3 11:01:16 2004")
        self.assertEqual(contig.reads[2].ds.chem, "term")
        self.assertEqual(contig.reads[2].ds.dye, "big")
        self.assertEqual(contig.reads[2].ds.template, "")
        self.assertEqual(contig.reads[2].ds.direction, "")
        self.assertIsNone(contig.reads[2].rt)
        self.assertIsNone(contig.reads[2].wr)

        # Read 3
        self.assertEqual(contig.reads[3].rd.name, "BL060-c1-LR17R.b.ab1")
        self.assertEqual(contig.reads[3].rd.padded_bases, 863)
        self.assertEqual(contig.reads[3].rd.info_items, 0)
        self.assertEqual(contig.reads[3].rd.read_tags, 0)
        center = len(contig.reads[3].rd.sequence) // 2
        self.assertEqual(contig.reads[3].rd.sequence[:10], "ctaattggcc")
        self.assertEqual(
            contig.reads[3].rd.sequence[center - 5 : center + 5], "GGAACCTTTC"
        )
        self.assertEqual(contig.reads[3].rd.sequence[-10:], "CAACCTgact")
        self.assertEqual(contig.reads[3].qa.qual_clipping_start, 63)
        self.assertEqual(contig.reads[3].qa.qual_clipping_end, 857)
        self.assertEqual(contig.reads[3].qa.align_clipping_start, 1)
        self.assertEqual(contig.reads[3].qa.align_clipping_end, 861)
        self.assertEqual(contig.reads[3].ds.chromat_file, "BL060-c1-LR17R.b.ab1")
        self.assertEqual(contig.reads[3].ds.phd_file, "BL060-c1-LR17R.b.ab1.phd.1")
        self.assertEqual(contig.reads[3].ds.time, "Tue Feb  3 11:01:16 2004")
        self.assertEqual(contig.reads[3].ds.chem, "term")
        self.assertEqual(contig.reads[3].ds.dye, "big")
        self.assertEqual(contig.reads[3].ds.template, "")
        self.assertEqual(contig.reads[3].ds.direction, "")
        self.assertEqual(len(contig.reads[3].rt), 1)
        self.assertEqual(contig.reads[3].rt[0].name, "BL060c3-LR5.g.ab1")
        self.assertEqual(contig.reads[3].rt[0].tag_type, "matchElsewhereHighQual")
        self.assertEqual(contig.reads[3].rt[0].program, "phrap")
        self.assertEqual(contig.reads[3].rt[0].padded_start, 617)
        self.assertEqual(contig.reads[3].rt[0].padded_end, 631)
        self.assertEqual(contig.reads[3].rt[0].date, "040217:110357")
        self.assertIsNone(contig.reads[3].wr)

        # Read 4
        self.assertEqual(contig.reads[4].rd.name, "BL060-LR8.5.g.ab1")
        self.assertEqual(contig.reads[4].rd.padded_bases, 877)
        self.assertEqual(contig.reads[4].rd.info_items, 0)
        self.assertEqual(contig.reads[4].rd.read_tags, 0)
        center = len(contig.reads[4].rd.sequence) // 2
        self.assertEqual(contig.reads[4].rd.sequence[:10], "tgCTGCGGTT")
        self.assertEqual(
            contig.reads[4].rd.sequence[center - 5 : center + 5], "GGCAGTTTCA"
        )
        self.assertEqual(contig.reads[4].rd.sequence[-10:], "tactcataaa")
        self.assertEqual(contig.reads[4].qa.qual_clipping_start, 13)
        self.assertEqual(contig.reads[4].qa.qual_clipping_end, 729)
        self.assertEqual(contig.reads[4].qa.align_clipping_start, 1)
        self.assertEqual(contig.reads[4].qa.align_clipping_end, 877)
        self.assertEqual(contig.reads[4].ds.chromat_file, "BL060-LR8.5.g.ab1")
        self.assertEqual(contig.reads[4].ds.phd_file, "BL060-LR8.5.g.ab1.phd.1")
        self.assertEqual(contig.reads[4].ds.time, "Fri Nov 14 09:46:03 2003")
        self.assertEqual(contig.reads[4].ds.chem, "term")
        self.assertEqual(contig.reads[4].ds.dye, "big")
        self.assertEqual(contig.reads[4].ds.template, "")
        self.assertEqual(contig.reads[4].ds.direction, "")
        self.assertIsNone(contig.reads[4].rt)
        self.assertIsNone(contig.reads[4].wr)

        # Read 5
        self.assertEqual(contig.reads[5].rd.name, "BL060-LR3R.b.ab1")
        self.assertEqual(contig.reads[5].rd.padded_bases, 874)
        self.assertEqual(contig.reads[5].rd.info_items, 0)
        self.assertEqual(contig.reads[5].rd.read_tags, 0)
        center = len(contig.reads[5].rd.sequence) // 2
        self.assertEqual(contig.reads[5].rd.sequence[:10], "ctCTTAGGAT")
        self.assertEqual(
            contig.reads[5].rd.sequence[center - 5 : center + 5], "AACTCACATT"
        )
        self.assertEqual(contig.reads[5].rd.sequence[-10:], "*CACCCAAac")
        self.assertEqual(contig.reads[5].qa.qual_clipping_start, 65)
        self.assertEqual(contig.reads[5].qa.qual_clipping_end, 874)
        self.assertEqual(contig.reads[5].qa.align_clipping_start, 1)
        self.assertEqual(contig.reads[5].qa.align_clipping_end, 874)
        self.assertEqual(contig.reads[5].ds.chromat_file, "BL060-LR3R.b.ab1")
        self.assertEqual(contig.reads[5].ds.phd_file, "BL060-LR3R.b.ab1.phd.1")
        self.assertEqual(contig.reads[5].ds.time, "Fri Nov 14 09:46:03 2003")
        self.assertEqual(contig.reads[5].ds.chem, "term")
        self.assertEqual(contig.reads[5].ds.dye, "big")
        self.assertEqual(contig.reads[5].ds.template, "")
        self.assertEqual(contig.reads[5].ds.direction, "")
        self.assertIsNone(contig.reads[5].rt)
        self.assertIsNone(contig.reads[5].wr)

        # Read 6
        self.assertEqual(contig.reads[6].rd.name, "BL060-c1-LR3R.b.ab1")
        self.assertEqual(contig.reads[6].rd.padded_bases, 864)
        self.assertEqual(contig.reads[6].rd.info_items, 0)
        self.assertEqual(contig.reads[6].rd.read_tags, 0)
        center = len(contig.reads[6].rd.sequence) // 2
        self.assertEqual(contig.reads[6].rd.sequence[:10], "CCaTGTCCAA")
        self.assertEqual(
            contig.reads[6].rd.sequence[center - 5 : center + 5], "AAGGGTT*CA"
        )
        self.assertEqual(contig.reads[6].rd.sequence[-10:], "ACACTCGCga")
        self.assertEqual(contig.reads[6].qa.qual_clipping_start, 73)
        self.assertEqual(contig.reads[6].qa.qual_clipping_end, 862)
        self.assertEqual(contig.reads[6].qa.align_clipping_start, 1)
        self.assertEqual(contig.reads[6].qa.align_clipping_end, 863)
        self.assertEqual(contig.reads[6].ds.chromat_file, "BL060-c1-LR3R.b.ab1")
        self.assertEqual(contig.reads[6].ds.phd_file, "BL060-c1-LR3R.b.ab1.phd.1")
        self.assertEqual(contig.reads[6].ds.time, "Tue Feb  3 11:01:16 2004")
        self.assertEqual(contig.reads[6].ds.chem, "term")
        self.assertEqual(contig.reads[6].ds.dye, "big")
        self.assertEqual(contig.reads[6].ds.template, "")
        self.assertEqual(contig.reads[6].ds.direction, "")
        self.assertIsNone(contig.reads[6].rt)
        self.assertIsNone(contig.reads[6].wr)

        # Read 7
        self.assertEqual(contig.reads[7].rd.name, "BL060-LR3R.b.ab1")
        self.assertEqual(contig.reads[7].rd.padded_bases, 857)
        self.assertEqual(contig.reads[7].rd.info_items, 0)
        self.assertEqual(contig.reads[7].rd.read_tags, 0)
        center = len(contig.reads[7].rd.sequence) // 2
        self.assertEqual(contig.reads[7].rd.sequence[:10], "agaaagagga")
        self.assertEqual(
            contig.reads[7].rd.sequence[center - 5 : center + 5], "nnnannnnnn"
        )
        self.assertEqual(contig.reads[7].rd.sequence[-10:], "gtctttgctc")
        self.assertEqual(contig.reads[7].qa.qual_clipping_start, 548)
        self.assertEqual(contig.reads[7].qa.qual_clipping_end, 847)
        self.assertEqual(contig.reads[7].qa.align_clipping_start, 442)
        self.assertEqual(contig.reads[7].qa.align_clipping_end, 854)
        self.assertEqual(contig.reads[7].ds.chromat_file, "BL060-LR3R.b.ab1")
        self.assertEqual(contig.reads[7].ds.phd_file, "BL060-LR3R.b.ab1.phd.1")
        self.assertEqual(contig.reads[7].ds.time, "Fri Jan 16 09:01:10 2004")
        self.assertEqual(contig.reads[7].ds.chem, "term")
        self.assertEqual(contig.reads[7].ds.dye, "big")
        self.assertEqual(contig.reads[7].ds.template, "")
        self.assertEqual(contig.reads[7].ds.direction, "")
        self.assertIsNone(contig.reads[7].rt)
        self.assertIsNone(contig.reads[7].wr)

        # Read 8
        self.assertEqual(contig.reads[8].rd.name, "BL060-c1-LR7.g.ab1")
        self.assertEqual(contig.reads[8].rd.padded_bases, 878)
        self.assertEqual(contig.reads[8].rd.info_items, 0)
        self.assertEqual(contig.reads[8].rd.read_tags, 0)
        center = len(contig.reads[8].rd.sequence) // 2
        self.assertEqual(contig.reads[8].rd.sequence[:10], "agTttc*ctc")
        self.assertEqual(
            contig.reads[8].rd.sequence[center - 5 : center + 5], "TCATAAAACT"
        )
        self.assertEqual(contig.reads[8].rd.sequence[-10:], "xxxxxxxxxx")
        self.assertEqual(contig.reads[8].qa.qual_clipping_start, 20)
        self.assertEqual(contig.reads[8].qa.qual_clipping_end, 798)
        self.assertEqual(contig.reads[8].qa.align_clipping_start, 1)
        self.assertEqual(contig.reads[8].qa.align_clipping_end, 798)
        self.assertEqual(contig.reads[8].ds.chromat_file, "BL060-c1-LR7.g.ab1")
        self.assertEqual(contig.reads[8].ds.phd_file, "BL060-c1-LR7.g.ab1.phd.1")
        self.assertEqual(contig.reads[8].ds.time, "Tue Feb  3 11:01:16 2004")
        self.assertEqual(contig.reads[8].ds.chem, "term")
        self.assertEqual(contig.reads[8].ds.dye, "big")
        self.assertEqual(contig.reads[8].ds.template, "")
        self.assertEqual(contig.reads[8].ds.direction, "")
        self.assertIsNone(contig.reads[8].rt)
        self.assertIsNone(contig.reads[8].wr)

        # Read 9
        self.assertEqual(contig.reads[9].rd.name, "BL060-LR7.g.ab1")
        self.assertEqual(contig.reads[9].rd.padded_bases, 880)
        self.assertEqual(contig.reads[9].rd.info_items, 0)
        self.assertEqual(contig.reads[9].rd.read_tags, 0)
        center = len(contig.reads[9].rd.sequence) // 2
        self.assertEqual(contig.reads[9].rd.sequence[:10], "ggctaCGCCc")
        self.assertEqual(
            contig.reads[9].rd.sequence[center - 5 : center + 5], "ATTGAGTTTC"
        )
        self.assertEqual(contig.reads[9].rd.sequence[-10:], "tggcgttgcg")
        self.assertEqual(contig.reads[9].qa.qual_clipping_start, 14)
        self.assertEqual(contig.reads[9].qa.qual_clipping_end, 765)
        self.assertEqual(contig.reads[9].qa.align_clipping_start, 4)
        self.assertEqual(contig.reads[9].qa.align_clipping_end, 765)
        self.assertEqual(contig.reads[9].ds.chromat_file, "BL060-LR7.g.ab1")
        self.assertEqual(contig.reads[9].ds.phd_file, "BL060-LR7.g.ab1.phd.1")
        self.assertEqual(contig.reads[9].ds.time, "Fri Nov 14 09:46:03 2003")
        self.assertEqual(contig.reads[9].ds.chem, "term")
        self.assertEqual(contig.reads[9].ds.dye, "big")
        self.assertEqual(contig.reads[9].ds.template, "")
        self.assertEqual(contig.reads[9].ds.direction, "")
        self.assertIsNone(contig.reads[9].rt)
        self.assertIsNone(contig.reads[9].wr)

        # Read 10
        self.assertEqual(contig.reads[10].rd.name, "BL060c5-LR5.g.ab1")
        self.assertEqual(contig.reads[10].rd.padded_bases, 871)
        self.assertEqual(contig.reads[10].rd.info_items, 0)
        self.assertEqual(contig.reads[10].rd.read_tags, 0)
        center = len(contig.reads[10].rd.sequence) // 2
        self.assertEqual(contig.reads[10].rd.sequence[:10], "ggtTCGATTA")
        self.assertEqual(
            contig.reads[10].rd.sequence[center - 5 : center + 5], "ACCAATTGAC"
        )
        self.assertEqual(contig.reads[10].rd.sequence[-10:], "ACCACCCatt")
        self.assertEqual(contig.reads[10].qa.qual_clipping_start, 12)
        self.assertEqual(contig.reads[10].qa.qual_clipping_end, 767)
        self.assertEqual(contig.reads[10].qa.align_clipping_start, 1)
        self.assertEqual(contig.reads[10].qa.align_clipping_end, 871)
        self.assertEqual(contig.reads[10].ds.chromat_file, "BL060c5-LR5.g.ab1")
        self.assertEqual(contig.reads[10].ds.phd_file, "BL060c5-LR5.g.ab1.phd.1")
        self.assertEqual(contig.reads[10].ds.time, "Fri Nov 14 09:46:03 2003")
        self.assertEqual(contig.reads[10].ds.chem, "term")
        self.assertEqual(contig.reads[10].ds.dye, "big")
        self.assertEqual(contig.reads[10].ds.template, "")
        self.assertEqual(contig.reads[10].ds.direction, "")
        self.assertIsNone(contig.reads[10].rt)
        self.assertIsNone(contig.reads[10].wr)

        # Read 11
        self.assertEqual(contig.reads[11].rd.name, "BL060c2-LR5.g.ab1")
        self.assertEqual(contig.reads[11].rd.padded_bases, 839)
        self.assertEqual(contig.reads[11].rd.info_items, 0)
        self.assertEqual(contig.reads[11].rd.read_tags, 0)
        center = len(contig.reads[11].rd.sequence) // 2
        self.assertEqual(contig.reads[11].rd.sequence[:10], "ggttcatatg")
        self.assertEqual(
            contig.reads[11].rd.sequence[center - 5 : center + 5], "TAAAATCAGT"
        )
        self.assertEqual(contig.reads[11].rd.sequence[-10:], "TCTTGCaata")
        self.assertEqual(contig.reads[11].qa.qual_clipping_start, 11)
        self.assertEqual(contig.reads[11].qa.qual_clipping_end, 757)
        self.assertEqual(contig.reads[11].qa.align_clipping_start, 10)
        self.assertEqual(contig.reads[11].qa.align_clipping_end, 835)
        self.assertIsNone(contig.reads[11].ds)
        self.assertEqual(len(contig.reads[11].rt), 1)
        self.assertEqual(contig.reads[11].rt[0].name, "BL060c2-LR5.g.ab1")
        self.assertEqual(contig.reads[11].rt[0].tag_type, "matchElsewhereHighQual")
        self.assertEqual(contig.reads[11].rt[0].program, "phrap")
        self.assertEqual(contig.reads[11].rt[0].padded_start, 617)
        self.assertEqual(contig.reads[11].rt[0].padded_end, 631)
        self.assertEqual(contig.reads[11].rt[0].date, "040217:110357")
        self.assertIsNone(contig.reads[11].wr)

        # Read 12
        self.assertEqual(contig.reads[12].rd.name, "BL060c5-LR0R.b.ab1")
        self.assertEqual(contig.reads[12].rd.padded_bases, 855)
        self.assertEqual(contig.reads[12].rd.info_items, 0)
        self.assertEqual(contig.reads[12].rd.read_tags, 0)
        center = len(contig.reads[12].rd.sequence) // 2
        self.assertEqual(contig.reads[12].rd.sequence[:10], "cACTCGCGTA")
        self.assertEqual(
            contig.reads[12].rd.sequence[center - 5 : center + 5], "CTCGTAAAAT"
        )
        self.assertEqual(contig.reads[12].rd.sequence[-10:], "aacccctgca")
        self.assertEqual(contig.reads[12].qa.qual_clipping_start, 94)
        self.assertEqual(contig.reads[12].qa.qual_clipping_end, 835)
        self.assertEqual(contig.reads[12].qa.align_clipping_start, 1)
        self.assertEqual(contig.reads[12].qa.align_clipping_end, 847)
        self.assertEqual(contig.reads[12].ds.chromat_file, "BL060c5-LR0R.b.ab1")
        self.assertEqual(contig.reads[12].ds.phd_file, "BL060c5-LR0R.b.ab1.phd.1")
        self.assertEqual(contig.reads[12].ds.time, "Wed Nov 12 08:16:30 2003")
        self.assertEqual(contig.reads[12].ds.chem, "term")
        self.assertEqual(contig.reads[12].ds.dye, "big")
        self.assertEqual(contig.reads[12].ds.template, "")
        self.assertEqual(contig.reads[12].ds.direction, "")
        self.assertIsNone(contig.reads[12].rt)
        self.assertIsNone(contig.reads[12].wr)

        # Read 13
        self.assertEqual(contig.reads[13].rd.name, "BL060c2-LR0R.b.ab1")
        self.assertEqual(contig.reads[13].rd.padded_bases, 852)
        self.assertEqual(contig.reads[13].rd.info_items, 0)
        self.assertEqual(contig.reads[13].rd.read_tags, 0)
        center = len(contig.reads[13].rd.sequence) // 2
        self.assertEqual(contig.reads[13].rd.sequence[:10], "cgCGTa*tTG")
        self.assertEqual(
            contig.reads[13].rd.sequence[center - 5 : center + 5], "GTAAAATATT"
        )
        self.assertEqual(contig.reads[13].rd.sequence[-10:], "Atccttgtag")
        self.assertEqual(contig.reads[13].qa.qual_clipping_start, 33)
        self.assertEqual(contig.reads[13].qa.qual_clipping_end, 831)
        self.assertEqual(contig.reads[13].qa.align_clipping_start, 1)
        self.assertEqual(contig.reads[13].qa.align_clipping_end, 852)
        self.assertEqual(contig.reads[13].ds.chromat_file, "BL060c2-LR0R.b.ab1")
        self.assertEqual(contig.reads[13].ds.phd_file, "BL060c2-LR0R.b.ab1.phd.1")
        self.assertEqual(contig.reads[13].ds.time, "Wed Nov 12 08:16:29 2003")
        self.assertEqual(contig.reads[13].ds.chem, "term")
        self.assertEqual(contig.reads[13].ds.dye, "big")
        self.assertEqual(contig.reads[13].ds.template, "")
        self.assertEqual(contig.reads[13].ds.direction, "")
        self.assertEqual(len(contig.reads[13].rt), 1)
        self.assertEqual(contig.reads[13].rt[0].name, "BL060c5-LR0R.b.ab1")
        self.assertEqual(contig.reads[13].rt[0].tag_type, "matchElsewhereHighQual")
        self.assertEqual(contig.reads[13].rt[0].program, "phrap")
        self.assertEqual(contig.reads[13].rt[0].padded_start, 617)
        self.assertEqual(contig.reads[13].rt[0].padded_end, 631)
        self.assertEqual(contig.reads[13].rt[0].date, "040217:110357")
        self.assertEqual(len(contig.reads[13].wr), 1)
        self.assertEqual(contig.reads[13].wr[0].name, "BL060c2-LR0R.b.ab1")
        self.assertEqual(contig.reads[13].wr[0].aligned, "unaligned")
        self.assertEqual(contig.reads[13].wr[0].program, "phrap")
        self.assertEqual(contig.reads[13].wr[0].date, "040217:110357")

        # Make sure there are no more contigs
        self.assertRaises(StopIteration, next, contigs)


class AceTestTwo(unittest.TestCase):
    """Test parsing example output from CAP3.

    The sample input file seq.cap.ace was downloaded from:
    http://genome.cs.mtu.edu/cap/data/seq.cap.ace
    """

    def setUp(self):
        self.handle = open("Ace/seq.cap.ace")

    def tearDown(self):
        self.handle.close()

    def test_check_ACEParser(self):
        """Test to check that ACEParser can parse the whole file into one record."""
        record = Ace.read(self.handle)
        self.assertEqual(record.ncontigs, 1)
        self.assertEqual(record.nreads, 6)
        self.assertIsNone(record.wa)
        self.assertEqual(len(record.contigs), 1)

        self.assertEqual(len(record.contigs[0].reads), 6)
        self.assertEqual(record.contigs[0].name, "Contig1")
        self.assertEqual(record.contigs[0].nbases, 1222)
        self.assertEqual(record.contigs[0].nreads, 6)
        self.assertEqual(record.contigs[0].nsegments, 0)
        self.assertEqual(record.contigs[0].uorc, "U")
        center = len(record.contigs[0].sequence) // 2
        self.assertEqual(record.contigs[0].sequence[:10], "AGTTTTAGTT")
        self.assertEqual(
            record.contigs[0].sequence[center - 5 : center + 5], "TGTGCGCGCA"
        )
        self.assertEqual(record.contigs[0].sequence[-10:], "ATATCACATT")
        center = len(record.contigs[0].quality) // 2
        self.assertEqual(
            record.contigs[0].quality[:10], [61, 66, 67, 70, 71, 73, 73, 77, 77, 87]
        )
        self.assertEqual(
            record.contigs[0].quality[center - 5 : center + 5],
            [97, 97, 97, 97, 97, 97, 97, 97, 97, 97],
        )
        self.assertEqual(
            record.contigs[0].quality[-10:], [56, 51, 49, 41, 38, 39, 45, 44, 49, 46]
        )
        self.assertEqual(len(record.contigs[0].af), 6)
        self.assertEqual(len(record.contigs[0].bs), 0)
        self.assertEqual(record.contigs[0].af[3].name, "R5")
        self.assertEqual(record.contigs[0].af[3].coru, "C")
        self.assertEqual(record.contigs[0].af[3].padded_start, 320)
        self.assertEqual(record.contigs[0].af[5].name, "R6")
        self.assertEqual(record.contigs[0].af[5].coru, "C")
        self.assertEqual(record.contigs[0].af[5].padded_start, 517)
        self.assertEqual(record.contigs[0].bs, [])
        self.assertIsNone(record.contigs[0].ct)
        self.assertIsNone(record.contigs[0].wa)
        self.assertEqual(len(record.contigs[0].reads), 6)

        self.assertEqual(record.contigs[0].reads[0].rd.name, "R3")
        self.assertEqual(record.contigs[0].reads[0].rd.padded_bases, 919)
        self.assertEqual(record.contigs[0].reads[0].rd.info_items, 0)
        self.assertEqual(record.contigs[0].reads[0].rd.read_tags, 0)
        center = len(record.contigs[0].reads[0].rd.sequence) // 2
        self.assertEqual(record.contigs[0].reads[0].rd.sequence[:10], "NNNNNNNNNN")
        self.assertEqual(
            record.contigs[0].reads[0].rd.sequence[center - 5 : center + 5],
            "ATGTGCGCTC",
        )
        self.assertEqual(record.contigs[0].reads[0].rd.sequence[-10:], "CAGCTCACCA")
        self.assertEqual(record.contigs[0].reads[0].qa.qual_clipping_start, 55)
        self.assertEqual(record.contigs[0].reads[0].qa.qual_clipping_end, 916)
        self.assertEqual(record.contigs[0].reads[0].qa.align_clipping_start, 55)
        self.assertEqual(record.contigs[0].reads[0].qa.align_clipping_end, 916)
        self.assertEqual(record.contigs[0].reads[0].ds.chromat_file, "")
        self.assertEqual(record.contigs[0].reads[0].ds.phd_file, "")
        self.assertEqual(record.contigs[0].reads[0].ds.time, "")
        self.assertEqual(record.contigs[0].reads[0].ds.chem, "")
        self.assertEqual(record.contigs[0].reads[0].ds.dye, "")
        self.assertEqual(record.contigs[0].reads[0].ds.template, "")
        self.assertEqual(record.contigs[0].reads[0].ds.direction, "")
        self.assertIsNone(record.contigs[0].reads[0].rt)
        self.assertIsNone(record.contigs[0].reads[0].wr)

        self.assertEqual(record.contigs[0].reads[1].rd.name, "R1")
        self.assertEqual(record.contigs[0].reads[1].rd.padded_bases, 864)
        self.assertEqual(record.contigs[0].reads[1].rd.info_items, 0)
        self.assertEqual(record.contigs[0].reads[1].rd.read_tags, 0)
        center = len(record.contigs[0].reads[1].rd.sequence) // 2
        self.assertEqual(record.contigs[0].reads[1].rd.sequence[:10], "AGCCGGTACC")
        self.assertEqual(
            record.contigs[0].reads[1].rd.sequence[center - 5 : center + 5],
            "GGGATGGCAC",
        )
        self.assertEqual(record.contigs[0].reads[1].rd.sequence[-10:], "GGGCTGGGAG")
        self.assertEqual(record.contigs[0].reads[1].qa.qual_clipping_start, 12)
        self.assertEqual(record.contigs[0].reads[1].qa.qual_clipping_end, 863)
        self.assertEqual(record.contigs[0].reads[1].qa.align_clipping_start, 12)
        self.assertEqual(record.contigs[0].reads[1].qa.align_clipping_end, 863)
        self.assertEqual(record.contigs[0].reads[1].ds.chromat_file, "")
        self.assertEqual(record.contigs[0].reads[1].ds.phd_file, "")
        self.assertEqual(record.contigs[0].reads[1].ds.time, "")
        self.assertEqual(record.contigs[0].reads[1].ds.chem, "")
        self.assertEqual(record.contigs[0].reads[1].ds.dye, "")
        self.assertEqual(record.contigs[0].reads[1].ds.template, "")
        self.assertEqual(record.contigs[0].reads[1].ds.direction, "")
        self.assertIsNone(record.contigs[0].reads[1].rt)
        self.assertIsNone(record.contigs[0].reads[1].wr)

        self.assertEqual(record.contigs[0].reads[2].rd.name, "R2")
        self.assertEqual(record.contigs[0].reads[2].rd.padded_bases, 1026)
        self.assertEqual(record.contigs[0].reads[2].rd.info_items, 0)
        self.assertEqual(record.contigs[0].reads[2].rd.read_tags, 0)
        center = len(record.contigs[0].reads[2].rd.sequence) // 2
        self.assertEqual(record.contigs[0].reads[2].rd.sequence[:10], "NNNNNNNNNN")
        self.assertEqual(
            record.contigs[0].reads[2].rd.sequence[center - 5 : center + 5],
            "GGATGCCTGG",
        )
        self.assertEqual(record.contigs[0].reads[2].rd.sequence[-10:], "GGTTGAGGCC")
        self.assertEqual(record.contigs[0].reads[2].qa.qual_clipping_start, 55)
        self.assertEqual(record.contigs[0].reads[2].qa.qual_clipping_end, 1000)
        self.assertEqual(record.contigs[0].reads[2].qa.align_clipping_start, 55)
        self.assertEqual(record.contigs[0].reads[2].qa.align_clipping_end, 1000)
        self.assertEqual(record.contigs[0].reads[2].ds.chromat_file, "")
        self.assertEqual(record.contigs[0].reads[2].ds.phd_file, "")
        self.assertEqual(record.contigs[0].reads[2].ds.time, "")
        self.assertEqual(record.contigs[0].reads[2].ds.chem, "")
        self.assertEqual(record.contigs[0].reads[2].ds.dye, "")
        self.assertEqual(record.contigs[0].reads[2].ds.template, "")
        self.assertEqual(record.contigs[0].reads[2].ds.direction, "")
        self.assertIsNone(record.contigs[0].reads[2].rt)
        self.assertIsNone(record.contigs[0].reads[2].wr)

        self.assertEqual(record.contigs[0].reads[3].rd.name, "R5")
        self.assertEqual(record.contigs[0].reads[3].rd.padded_bases, 925)
        self.assertEqual(record.contigs[0].reads[3].rd.info_items, 0)
        self.assertEqual(record.contigs[0].reads[3].rd.read_tags, 0)
        center = len(record.contigs[0].reads[3].rd.sequence) // 2
        self.assertEqual(record.contigs[0].reads[3].rd.sequence[:10], "NNNNNNNNNN")
        self.assertEqual(
            record.contigs[0].reads[3].rd.sequence[center - 5 : center + 5],
            "CCTCCCTACA",
        )
        self.assertEqual(record.contigs[0].reads[3].rd.sequence[-10:], "GCCCCCGGNN")
        self.assertEqual(record.contigs[0].reads[3].qa.qual_clipping_start, 293)
        self.assertEqual(record.contigs[0].reads[3].qa.qual_clipping_end, 874)
        self.assertEqual(record.contigs[0].reads[3].qa.align_clipping_start, 293)
        self.assertEqual(record.contigs[0].reads[3].qa.align_clipping_end, 874)
        self.assertEqual(record.contigs[0].reads[3].ds.chromat_file, "")
        self.assertEqual(record.contigs[0].reads[3].ds.phd_file, "")
        self.assertEqual(record.contigs[0].reads[3].ds.time, "")
        self.assertEqual(record.contigs[0].reads[3].ds.chem, "")
        self.assertEqual(record.contigs[0].reads[3].ds.dye, "")
        self.assertEqual(record.contigs[0].reads[3].ds.template, "")
        self.assertEqual(record.contigs[0].reads[3].ds.direction, "")
        self.assertIsNone(record.contigs[0].reads[3].rt)
        self.assertIsNone(record.contigs[0].reads[3].wr)

        self.assertEqual(record.contigs[0].reads[4].rd.name, "R4")
        self.assertEqual(record.contigs[0].reads[4].rd.padded_bases, 816)
        self.assertEqual(record.contigs[0].reads[4].rd.info_items, 0)
        self.assertEqual(record.contigs[0].reads[4].rd.read_tags, 0)
        center = len(record.contigs[0].reads[4].rd.sequence) // 2
        self.assertEqual(record.contigs[0].reads[4].rd.sequence[:10], "CACTCAGCTC")
        self.assertEqual(
            record.contigs[0].reads[4].rd.sequence[center - 5 : center + 5],
            "TCCAAAGGGT",
        )
        self.assertEqual(record.contigs[0].reads[4].rd.sequence[-10:], "AGCTGAATCG")
        self.assertEqual(record.contigs[0].reads[4].qa.qual_clipping_start, 1)
        self.assertEqual(record.contigs[0].reads[4].qa.qual_clipping_end, 799)
        self.assertEqual(record.contigs[0].reads[4].qa.align_clipping_start, 1)
        self.assertEqual(record.contigs[0].reads[4].qa.align_clipping_end, 799)
        self.assertEqual(record.contigs[0].reads[4].ds.chromat_file, "")
        self.assertEqual(record.contigs[0].reads[4].ds.phd_file, "")
        self.assertEqual(record.contigs[0].reads[4].ds.time, "")
        self.assertEqual(record.contigs[0].reads[4].ds.chem, "")
        self.assertEqual(record.contigs[0].reads[4].ds.dye, "")
        self.assertEqual(record.contigs[0].reads[4].ds.template, "")
        self.assertEqual(record.contigs[0].reads[4].ds.direction, "")
        self.assertIsNone(record.contigs[0].reads[4].rt)
        self.assertIsNone(record.contigs[0].reads[4].wr)

        self.assertEqual(record.contigs[0].reads[5].rd.name, "R6")
        self.assertEqual(record.contigs[0].reads[5].rd.padded_bases, 857)
        self.assertEqual(record.contigs[0].reads[5].rd.info_items, 0)
        self.assertEqual(record.contigs[0].reads[5].rd.read_tags, 0)
        center = len(record.contigs[0].reads[5].rd.sequence) // 2
        self.assertEqual(record.contigs[0].reads[5].rd.sequence[:10], "CCGGCAGTGA")
        self.assertEqual(
            record.contigs[0].reads[5].rd.sequence[center - 5 : center + 5],
            "AAAAAAAACC",
        )
        self.assertEqual(record.contigs[0].reads[5].rd.sequence[-10:], "NNNNNNNNNN")
        self.assertEqual(record.contigs[0].reads[5].qa.qual_clipping_start, 24)
        self.assertEqual(record.contigs[0].reads[5].qa.qual_clipping_end, 706)
        self.assertEqual(record.contigs[0].reads[5].qa.align_clipping_start, 24)
        self.assertEqual(record.contigs[0].reads[5].qa.align_clipping_end, 706)
        self.assertEqual(record.contigs[0].reads[5].ds.chromat_file, "")
        self.assertEqual(record.contigs[0].reads[5].ds.phd_file, "")
        self.assertEqual(record.contigs[0].reads[5].ds.time, "")
        self.assertEqual(record.contigs[0].reads[5].ds.chem, "")
        self.assertEqual(record.contigs[0].reads[5].ds.dye, "")
        self.assertEqual(record.contigs[0].reads[5].ds.template, "")
        self.assertEqual(record.contigs[0].reads[5].ds.direction, "")
        self.assertIsNone(record.contigs[0].reads[5].rt)
        self.assertIsNone(record.contigs[0].reads[5].wr)

    def test_check_record_parser(self):
        """Test to check that record parser parses each contig into a record."""
        contigs = Ace.parse(self.handle)

        # First (and only) contig
        contig = next(contigs)

        self.assertEqual(len(contig.reads), 6)
        self.assertEqual(contig.name, "Contig1")
        self.assertEqual(contig.nbases, 1222)
        self.assertEqual(contig.nreads, 6)
        self.assertEqual(contig.nsegments, 0)
        self.assertEqual(contig.uorc, "U")
        center = len(contig.sequence) // 2
        self.assertEqual(contig.sequence[:10], "AGTTTTAGTT")
        self.assertEqual(contig.sequence[center - 5 : center + 5], "TGTGCGCGCA")
        self.assertEqual(contig.sequence[-10:], "ATATCACATT")
        center = len(contig.quality) // 2
        self.assertEqual(contig.quality[:10], [61, 66, 67, 70, 71, 73, 73, 77, 77, 87])
        self.assertEqual(
            contig.quality[center - 5 : center + 5],
            [97, 97, 97, 97, 97, 97, 97, 97, 97, 97],
        )
        self.assertEqual(contig.quality[-10:], [56, 51, 49, 41, 38, 39, 45, 44, 49, 46])
        self.assertEqual(len(contig.af), 6)
        self.assertEqual(len(contig.bs), 0)
        self.assertEqual(contig.af[3].name, "R5")
        self.assertEqual(contig.af[3].coru, "C")
        self.assertEqual(contig.af[3].padded_start, 320)
        self.assertEqual(contig.af[5].name, "R6")
        self.assertEqual(contig.af[5].coru, "C")
        self.assertEqual(contig.af[5].padded_start, 517)
        self.assertEqual(contig.bs, [])
        self.assertIsNone(contig.ct)
        self.assertIsNone(contig.wa)
        self.assertEqual(len(contig.reads), 6)

        self.assertEqual(contig.reads[0].rd.name, "R3")
        self.assertEqual(contig.reads[0].rd.padded_bases, 919)
        self.assertEqual(contig.reads[0].rd.info_items, 0)
        self.assertEqual(contig.reads[0].rd.read_tags, 0)
        center = len(contig.reads[0].rd.sequence) // 2
        self.assertEqual(contig.reads[0].rd.sequence[:10], "NNNNNNNNNN")
        self.assertEqual(
            contig.reads[0].rd.sequence[center - 5 : center + 5], "ATGTGCGCTC"
        )
        self.assertEqual(contig.reads[0].rd.sequence[-10:], "CAGCTCACCA")
        self.assertEqual(contig.reads[0].qa.qual_clipping_start, 55)
        self.assertEqual(contig.reads[0].qa.qual_clipping_end, 916)
        self.assertEqual(contig.reads[0].qa.align_clipping_start, 55)
        self.assertEqual(contig.reads[0].qa.align_clipping_end, 916)
        self.assertEqual(contig.reads[0].ds.chromat_file, "")
        self.assertEqual(contig.reads[0].ds.phd_file, "")
        self.assertEqual(contig.reads[0].ds.time, "")
        self.assertEqual(contig.reads[0].ds.chem, "")
        self.assertEqual(contig.reads[0].ds.dye, "")
        self.assertEqual(contig.reads[0].ds.template, "")
        self.assertEqual(contig.reads[0].ds.direction, "")
        self.assertIsNone(contig.reads[0].rt)
        self.assertIsNone(contig.reads[0].wr)

        self.assertEqual(contig.reads[1].rd.name, "R1")
        self.assertEqual(contig.reads[1].rd.padded_bases, 864)
        self.assertEqual(contig.reads[1].rd.info_items, 0)
        self.assertEqual(contig.reads[1].rd.read_tags, 0)
        center = len(contig.reads[1].rd.sequence) // 2
        self.assertEqual(contig.reads[1].rd.sequence[:10], "AGCCGGTACC")
        self.assertEqual(
            contig.reads[1].rd.sequence[center - 5 : center + 5], "GGGATGGCAC"
        )
        self.assertEqual(contig.reads[1].rd.sequence[-10:], "GGGCTGGGAG")
        self.assertEqual(contig.reads[1].qa.qual_clipping_start, 12)
        self.assertEqual(contig.reads[1].qa.qual_clipping_end, 863)
        self.assertEqual(contig.reads[1].qa.align_clipping_start, 12)
        self.assertEqual(contig.reads[1].qa.align_clipping_end, 863)
        self.assertEqual(contig.reads[1].ds.chromat_file, "")
        self.assertEqual(contig.reads[1].ds.phd_file, "")
        self.assertEqual(contig.reads[1].ds.time, "")
        self.assertEqual(contig.reads[1].ds.chem, "")
        self.assertEqual(contig.reads[1].ds.dye, "")
        self.assertEqual(contig.reads[1].ds.template, "")
        self.assertEqual(contig.reads[1].ds.direction, "")
        self.assertIsNone(contig.reads[1].rt)
        self.assertIsNone(contig.reads[1].wr)

        self.assertEqual(contig.reads[2].rd.name, "R2")
        self.assertEqual(contig.reads[2].rd.padded_bases, 1026)
        self.assertEqual(contig.reads[2].rd.info_items, 0)
        self.assertEqual(contig.reads[2].rd.read_tags, 0)
        center = len(contig.reads[2].rd.sequence) // 2
        self.assertEqual(contig.reads[2].rd.sequence[:10], "NNNNNNNNNN")
        self.assertEqual(
            contig.reads[2].rd.sequence[center - 5 : center + 5], "GGATGCCTGG"
        )
        self.assertEqual(contig.reads[2].rd.sequence[-10:], "GGTTGAGGCC")
        self.assertEqual(contig.reads[2].qa.qual_clipping_start, 55)
        self.assertEqual(contig.reads[2].qa.qual_clipping_end, 1000)
        self.assertEqual(contig.reads[2].qa.align_clipping_start, 55)
        self.assertEqual(contig.reads[2].qa.align_clipping_end, 1000)
        self.assertEqual(contig.reads[2].ds.chromat_file, "")
        self.assertEqual(contig.reads[2].ds.phd_file, "")
        self.assertEqual(contig.reads[2].ds.time, "")
        self.assertEqual(contig.reads[2].ds.chem, "")
        self.assertEqual(contig.reads[2].ds.dye, "")
        self.assertEqual(contig.reads[2].ds.template, "")
        self.assertEqual(contig.reads[2].ds.direction, "")
        self.assertIsNone(contig.reads[2].rt)
        self.assertIsNone(contig.reads[2].wr)

        self.assertEqual(contig.reads[3].rd.name, "R5")
        self.assertEqual(contig.reads[3].rd.padded_bases, 925)
        self.assertEqual(contig.reads[3].rd.info_items, 0)
        self.assertEqual(contig.reads[3].rd.read_tags, 0)
        center = len(contig.reads[3].rd.sequence) // 2
        self.assertEqual(contig.reads[3].rd.sequence[:10], "NNNNNNNNNN")
        self.assertEqual(
            contig.reads[3].rd.sequence[center - 5 : center + 5], "CCTCCCTACA"
        )
        self.assertEqual(contig.reads[3].rd.sequence[-10:], "GCCCCCGGNN")
        self.assertEqual(contig.reads[3].qa.qual_clipping_start, 293)
        self.assertEqual(contig.reads[3].qa.qual_clipping_end, 874)
        self.assertEqual(contig.reads[3].qa.align_clipping_start, 293)
        self.assertEqual(contig.reads[3].qa.align_clipping_end, 874)
        self.assertEqual(contig.reads[3].ds.chromat_file, "")
        self.assertEqual(contig.reads[3].ds.phd_file, "")
        self.assertEqual(contig.reads[3].ds.time, "")
        self.assertEqual(contig.reads[3].ds.chem, "")
        self.assertEqual(contig.reads[3].ds.dye, "")
        self.assertEqual(contig.reads[3].ds.template, "")
        self.assertEqual(contig.reads[3].ds.direction, "")
        self.assertIsNone(contig.reads[3].rt)
        self.assertIsNone(contig.reads[3].wr)

        self.assertEqual(contig.reads[4].rd.name, "R4")
        self.assertEqual(contig.reads[4].rd.padded_bases, 816)
        self.assertEqual(contig.reads[4].rd.info_items, 0)
        self.assertEqual(contig.reads[4].rd.read_tags, 0)
        center = len(contig.reads[4].rd.sequence) // 2
        self.assertEqual(contig.reads[4].rd.sequence[:10], "CACTCAGCTC")
        self.assertEqual(
            contig.reads[4].rd.sequence[center - 5 : center + 5], "TCCAAAGGGT"
        )
        self.assertEqual(contig.reads[4].rd.sequence[-10:], "AGCTGAATCG")
        self.assertEqual(contig.reads[4].qa.qual_clipping_start, 1)
        self.assertEqual(contig.reads[4].qa.qual_clipping_end, 799)
        self.assertEqual(contig.reads[4].qa.align_clipping_start, 1)
        self.assertEqual(contig.reads[4].qa.align_clipping_end, 799)
        self.assertEqual(contig.reads[4].ds.chromat_file, "")
        self.assertEqual(contig.reads[4].ds.phd_file, "")
        self.assertEqual(contig.reads[4].ds.time, "")
        self.assertEqual(contig.reads[4].ds.chem, "")
        self.assertEqual(contig.reads[4].ds.dye, "")
        self.assertEqual(contig.reads[4].ds.template, "")
        self.assertEqual(contig.reads[4].ds.direction, "")
        self.assertIsNone(contig.reads[4].rt)
        self.assertIsNone(contig.reads[4].wr)

        self.assertEqual(contig.reads[5].rd.name, "R6")
        self.assertEqual(contig.reads[5].rd.padded_bases, 857)
        self.assertEqual(contig.reads[5].rd.info_items, 0)
        self.assertEqual(contig.reads[5].rd.read_tags, 0)
        center = len(contig.reads[5].rd.sequence) // 2
        self.assertEqual(contig.reads[5].rd.sequence[:10], "CCGGCAGTGA")
        self.assertEqual(
            contig.reads[5].rd.sequence[center - 5 : center + 5], "AAAAAAAACC"
        )
        self.assertEqual(contig.reads[5].rd.sequence[-10:], "NNNNNNNNNN")
        self.assertEqual(contig.reads[5].qa.qual_clipping_start, 24)
        self.assertEqual(contig.reads[5].qa.qual_clipping_end, 706)
        self.assertEqual(contig.reads[5].qa.align_clipping_start, 24)
        self.assertEqual(contig.reads[5].qa.align_clipping_end, 706)
        self.assertEqual(contig.reads[5].ds.chromat_file, "")
        self.assertEqual(contig.reads[5].ds.phd_file, "")
        self.assertEqual(contig.reads[5].ds.time, "")
        self.assertEqual(contig.reads[5].ds.chem, "")
        self.assertEqual(contig.reads[5].ds.dye, "")
        self.assertEqual(contig.reads[5].ds.template, "")
        self.assertEqual(contig.reads[5].ds.direction, "")
        self.assertIsNone(contig.reads[5].rt)
        self.assertIsNone(contig.reads[5].wr)

        # Make sure there are no more contigs
        self.assertRaises(StopIteration, next, contigs)


class AceTestThree(unittest.TestCase):
    """Test parsing example ACE input file for CONSED.

    The sample input file was downloaded from:
    http://bozeman.mbt.washington.edu/consed/distributions/README.16.0.txt
    """

    def setUp(self):
        self.handle = open("Ace/consed_sample.ace")

    def tearDown(self):
        self.handle.close()

    def test_check_ACEParser(self):
        """Test to check that ACEParser can parse the whole file into one record."""
        record = Ace.read(self.handle)
        self.assertEqual(record.ncontigs, 1)
        self.assertEqual(record.nreads, 8)
        self.assertEqual(len(record.wa), 1)
        self.assertEqual(record.wa[0].tag_type, "phrap_params")
        self.assertEqual(record.wa[0].program, "phrap")
        self.assertEqual(record.wa[0].date, "990621:161947")
        self.assertEqual(
            record.wa[0].info,
            [
                "/usr/local/genome/bin/phrap standard.fasta.screen -new_ace -view",
                "phrap version 0.990319",
            ],
        )
        self.assertEqual(len(record.contigs), 1)

        self.assertEqual(len(record.contigs[0].reads), 8)
        self.assertEqual(record.contigs[0].name, "Contig1")
        self.assertEqual(record.contigs[0].nbases, 1475)
        self.assertEqual(record.contigs[0].nreads, 8)
        self.assertEqual(record.contigs[0].nsegments, 156)
        self.assertEqual(record.contigs[0].uorc, "U")
        center = len(record.contigs[0].sequence) // 2
        self.assertEqual(record.contigs[0].sequence[:10], "agccccgggc")
        self.assertEqual(
            record.contigs[0].sequence[center - 5 : center + 5], "CTTCCCCAGG"
        )
        self.assertEqual(record.contigs[0].sequence[-10:], "gttgggtttg")
        center = len(record.contigs[0].quality) // 2
        self.assertEqual(record.contigs[0].quality[:10], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(
            record.contigs[0].quality[center - 5 : center + 5],
            [90, 90, 90, 90, 90, 90, 90, 90, 89, 89],
        )
        self.assertEqual(
            record.contigs[0].quality[-10:], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        )
        self.assertEqual(len(record.contigs[0].af), 8)
        self.assertEqual(len(record.contigs[0].bs), 156)
        self.assertEqual(record.contigs[0].af[4].name, "K26-291s")
        self.assertEqual(record.contigs[0].af[4].coru, "U")
        self.assertEqual(record.contigs[0].af[4].padded_start, 828)
        self.assertEqual(record.contigs[0].af[7].name, "K26-766c")
        self.assertEqual(record.contigs[0].af[7].coru, "C")
        self.assertEqual(record.contigs[0].af[7].padded_start, 408)
        self.assertEqual(record.contigs[0].bs[78].name, "K26-394c")
        self.assertEqual(record.contigs[0].bs[78].padded_start, 987)
        self.assertEqual(record.contigs[0].bs[78].padded_end, 987)
        self.assertEqual(record.contigs[0].bs[155].name, "K26-822c")
        self.assertEqual(record.contigs[0].bs[155].padded_start, 1303)
        self.assertEqual(record.contigs[0].bs[155].padded_end, 1475)
        self.assertEqual(len(record.contigs[0].ct), 3)
        self.assertEqual(record.contigs[0].ct[0].name, "Contig1")
        self.assertEqual(record.contigs[0].ct[0].tag_type, "repeat")
        self.assertEqual(record.contigs[0].ct[0].program, "consed")
        self.assertEqual(record.contigs[0].ct[0].padded_start, 976)
        self.assertEqual(record.contigs[0].ct[0].padded_end, 986)
        self.assertEqual(record.contigs[0].ct[0].date, "971218:180623")
        self.assertEqual(record.contigs[0].ct[0].info, [])
        self.assertEqual(record.contigs[0].ct[1].name, "Contig1")
        self.assertEqual(record.contigs[0].ct[1].tag_type, "comment")
        self.assertEqual(record.contigs[0].ct[1].program, "consed")
        self.assertEqual(record.contigs[0].ct[1].padded_start, 996)
        self.assertEqual(record.contigs[0].ct[1].padded_end, 1007)
        self.assertEqual(record.contigs[0].ct[1].date, "971218:180623")
        self.assertEqual(
            record.contigs[0].ct[1].info,
            ["This is line 1 of a comment", "There may be any number of lines"],
        )
        self.assertEqual(record.contigs[0].ct[2].name, "Contig1")
        self.assertEqual(record.contigs[0].ct[2].tag_type, "oligo")
        self.assertEqual(record.contigs[0].ct[2].program, "consed")
        self.assertEqual(record.contigs[0].ct[2].padded_start, 963)
        self.assertEqual(record.contigs[0].ct[2].padded_end, 987)
        self.assertEqual(record.contigs[0].ct[2].date, "971218:180623")
        self.assertEqual(
            record.contigs[0].ct[2].info,
            ["standard.1 acataagacattctaaatttttact 50 U", "seq from clone"],
        )
        self.assertEqual(len(record.contigs[0].wa), 1)
        self.assertEqual(record.contigs[0].wa[0].tag_type, "phrap_params")
        self.assertEqual(record.contigs[0].wa[0].program, "phrap")
        self.assertEqual(record.contigs[0].wa[0].date, "990621:161947")
        self.assertEqual(
            record.contigs[0].wa[0].info,
            [
                "/usr/local/genome/bin/phrap standard.fasta.screen -new_ace -view",
                "phrap version 0.990319",
            ],
        )

        self.assertEqual(len(record.contigs[0].reads), 8)

        self.assertEqual(record.contigs[0].reads[0].rd.name, "K26-217c")
        self.assertEqual(record.contigs[0].reads[0].rd.padded_bases, 563)
        self.assertEqual(record.contigs[0].reads[0].rd.info_items, 0)
        self.assertEqual(record.contigs[0].reads[0].rd.read_tags, 0)
        center = len(record.contigs[0].reads[0].rd.sequence) // 2
        self.assertEqual(record.contigs[0].reads[0].rd.sequence[:10], "tcccCgtgag")
        self.assertEqual(
            record.contigs[0].reads[0].rd.sequence[center - 5 : center + 5],
            "CTCCTGcctg",
        )
        self.assertEqual(record.contigs[0].reads[0].rd.sequence[-10:], "ggcccccctc")
        self.assertEqual(record.contigs[0].reads[0].qa.qual_clipping_start, 19)
        self.assertEqual(record.contigs[0].reads[0].qa.qual_clipping_end, 349)
        self.assertEqual(record.contigs[0].reads[0].qa.align_clipping_start, 19)
        self.assertEqual(record.contigs[0].reads[0].qa.align_clipping_end, 424)
        self.assertEqual(record.contigs[0].reads[0].ds.chromat_file, "K26-217c")
        self.assertEqual(record.contigs[0].reads[0].ds.phd_file, "K26-217c.phd.1")
        self.assertEqual(record.contigs[0].reads[0].ds.time, "Thu Sep 12 15:42:38 1996")
        self.assertEqual(record.contigs[0].reads[0].ds.chem, "")
        self.assertEqual(record.contigs[0].reads[0].ds.dye, "")
        self.assertEqual(record.contigs[0].reads[0].ds.template, "")
        self.assertEqual(record.contigs[0].reads[0].ds.direction, "")
        self.assertIsNone(record.contigs[0].reads[0].rt)
        self.assertIsNone(record.contigs[0].reads[0].wr)

        self.assertEqual(record.contigs[0].reads[1].rd.name, "K26-526t")
        self.assertEqual(record.contigs[0].reads[1].rd.padded_bases, 687)
        self.assertEqual(record.contigs[0].reads[1].rd.info_items, 0)
        self.assertEqual(record.contigs[0].reads[1].rd.read_tags, 0)
        center = len(record.contigs[0].reads[1].rd.sequence) // 2
        self.assertEqual(record.contigs[0].reads[1].rd.sequence[:10], "ccgtcctgag")
        self.assertEqual(
            record.contigs[0].reads[1].rd.sequence[center - 5 : center + 5],
            "cacagcccT*",
        )
        self.assertEqual(record.contigs[0].reads[1].rd.sequence[-10:], "Ttttgtttta")
        self.assertEqual(record.contigs[0].reads[1].qa.qual_clipping_start, 12)
        self.assertEqual(record.contigs[0].reads[1].qa.qual_clipping_end, 353)
        self.assertEqual(record.contigs[0].reads[1].qa.align_clipping_start, 9)
        self.assertEqual(record.contigs[0].reads[1].qa.align_clipping_end, 572)
        self.assertEqual(record.contigs[0].reads[1].ds.chromat_file, "K26-526t")
        self.assertEqual(record.contigs[0].reads[1].ds.phd_file, "K26-526t.phd.1")
        self.assertEqual(record.contigs[0].reads[1].ds.time, "Thu Sep 12 15:42:33 1996")
        self.assertEqual(record.contigs[0].reads[1].ds.chem, "")
        self.assertEqual(record.contigs[0].reads[1].ds.dye, "")
        self.assertEqual(record.contigs[0].reads[1].ds.template, "")
        self.assertEqual(record.contigs[0].reads[1].ds.direction, "")
        self.assertIsNone(record.contigs[0].reads[1].rt)
        self.assertIsNone(record.contigs[0].reads[1].wr)

        self.assertEqual(record.contigs[0].reads[2].rd.name, "K26-961c")
        self.assertEqual(record.contigs[0].reads[2].rd.padded_bases, 517)
        self.assertEqual(record.contigs[0].reads[2].rd.info_items, 0)
        self.assertEqual(record.contigs[0].reads[2].rd.read_tags, 0)
        center = len(record.contigs[0].reads[2].rd.sequence) // 2
        self.assertEqual(record.contigs[0].reads[2].rd.sequence[:10], "aatattaccg")
        self.assertEqual(
            record.contigs[0].reads[2].rd.sequence[center - 5 : center + 5],
            "CAGATGGGTT",
        )
        self.assertEqual(record.contigs[0].reads[2].rd.sequence[-10:], "ctattcaggg")
        self.assertEqual(record.contigs[0].reads[2].qa.qual_clipping_start, 20)
        self.assertEqual(record.contigs[0].reads[2].qa.qual_clipping_end, 415)
        self.assertEqual(record.contigs[0].reads[2].qa.align_clipping_start, 26)
        self.assertEqual(record.contigs[0].reads[2].qa.align_clipping_end, 514)
        self.assertEqual(record.contigs[0].reads[2].ds.chromat_file, "K26-961c")
        self.assertEqual(record.contigs[0].reads[2].ds.phd_file, "K26-961c.phd.1")
        self.assertEqual(record.contigs[0].reads[2].ds.time, "Thu Sep 12 15:42:37 1996")
        self.assertEqual(record.contigs[0].reads[2].ds.chem, "")
        self.assertEqual(record.contigs[0].reads[2].ds.dye, "")
        self.assertEqual(record.contigs[0].reads[2].ds.template, "")
        self.assertEqual(record.contigs[0].reads[2].ds.direction, "")
        self.assertIsNone(record.contigs[0].reads[2].rt)
        self.assertIsNone(record.contigs[0].reads[2].wr)

        self.assertEqual(record.contigs[0].reads[3].rd.name, "K26-394c")
        self.assertEqual(record.contigs[0].reads[3].rd.padded_bases, 628)
        self.assertEqual(record.contigs[0].reads[3].rd.info_items, 0)
        self.assertEqual(record.contigs[0].reads[3].rd.read_tags, 0)
        center = len(record.contigs[0].reads[3].rd.sequence) // 2
        self.assertEqual(record.contigs[0].reads[3].rd.sequence[:10], "ctgcgtatcg")
        self.assertEqual(
            record.contigs[0].reads[3].rd.sequence[center - 5 : center + 5],
            "AGGATTGCTT",
        )
        self.assertEqual(record.contigs[0].reads[3].rd.sequence[-10:], "aaccctgggt")
        self.assertEqual(record.contigs[0].reads[3].qa.qual_clipping_start, 18)
        self.assertEqual(record.contigs[0].reads[3].qa.qual_clipping_end, 368)
        self.assertEqual(record.contigs[0].reads[3].qa.align_clipping_start, 11)
        self.assertEqual(record.contigs[0].reads[3].qa.align_clipping_end, 502)
        self.assertEqual(record.contigs[0].reads[3].ds.chromat_file, "K26-394c")
        self.assertEqual(record.contigs[0].reads[3].ds.phd_file, "K26-394c.phd.1")
        self.assertEqual(record.contigs[0].reads[3].ds.time, "Thu Sep 12 15:42:32 1996")
        self.assertEqual(record.contigs[0].reads[3].ds.chem, "")
        self.assertEqual(record.contigs[0].reads[3].ds.dye, "")
        self.assertEqual(record.contigs[0].reads[3].ds.template, "")
        self.assertEqual(record.contigs[0].reads[3].ds.direction, "")
        self.assertIsNone(record.contigs[0].reads[3].rt)
        self.assertIsNone(record.contigs[0].reads[3].wr)

        self.assertEqual(record.contigs[0].reads[4].rd.name, "K26-291s")
        self.assertEqual(record.contigs[0].reads[4].rd.padded_bases, 556)
        self.assertEqual(record.contigs[0].reads[4].rd.info_items, 0)
        self.assertEqual(record.contigs[0].reads[4].rd.read_tags, 0)
        center = len(record.contigs[0].reads[4].rd.sequence) // 2
        self.assertEqual(record.contigs[0].reads[4].rd.sequence[:10], "gaggatcgct")
        self.assertEqual(
            record.contigs[0].reads[4].rd.sequence[center - 5 : center + 5],
            "GTgcgaggat",
        )
        self.assertEqual(record.contigs[0].reads[4].rd.sequence[-10:], "caggcagatg")
        self.assertEqual(record.contigs[0].reads[4].qa.qual_clipping_start, 11)
        self.assertEqual(record.contigs[0].reads[4].qa.qual_clipping_end, 373)
        self.assertEqual(record.contigs[0].reads[4].qa.align_clipping_start, 11)
        self.assertEqual(record.contigs[0].reads[4].qa.align_clipping_end, 476)
        self.assertEqual(record.contigs[0].reads[4].ds.chromat_file, "K26-291s")
        self.assertEqual(record.contigs[0].reads[4].ds.phd_file, "K26-291s.phd.1")
        self.assertEqual(record.contigs[0].reads[4].ds.time, "Thu Sep 12 15:42:31 1996")
        self.assertEqual(record.contigs[0].reads[4].ds.chem, "")
        self.assertEqual(record.contigs[0].reads[4].ds.dye, "")
        self.assertEqual(record.contigs[0].reads[4].ds.template, "")
        self.assertEqual(record.contigs[0].reads[4].ds.direction, "")
        self.assertIsNone(record.contigs[0].reads[4].rt)
        self.assertIsNone(record.contigs[0].reads[4].wr)

        self.assertEqual(record.contigs[0].reads[5].rd.name, "K26-822c")
        self.assertEqual(record.contigs[0].reads[5].rd.padded_bases, 593)
        self.assertEqual(record.contigs[0].reads[5].rd.info_items, 0)
        self.assertEqual(record.contigs[0].reads[5].rd.read_tags, 0)
        center = len(record.contigs[0].reads[5].rd.sequence) // 2
        self.assertEqual(record.contigs[0].reads[5].rd.sequence[:10], "ggggatccg*")
        self.assertEqual(
            record.contigs[0].reads[5].rd.sequence[center - 5 : center + 5],
            "GCaAgacCCt",
        )
        self.assertEqual(record.contigs[0].reads[5].rd.sequence[-10:], "gttgggtttg")

        self.assertEqual(record.contigs[0].reads[5].qa.qual_clipping_start, 25)
        self.assertEqual(record.contigs[0].reads[5].qa.qual_clipping_end, 333)
        self.assertEqual(record.contigs[0].reads[5].qa.align_clipping_start, 16)
        self.assertEqual(record.contigs[0].reads[5].qa.align_clipping_end, 593)
        self.assertEqual(record.contigs[0].reads[5].ds.chromat_file, "K26-822c")
        self.assertEqual(record.contigs[0].reads[5].ds.phd_file, "K26-822c.phd.1")
        self.assertEqual(record.contigs[0].reads[5].ds.time, "Thu Sep 12 15:42:36 1996")
        self.assertEqual(record.contigs[0].reads[5].ds.chem, "")
        self.assertEqual(record.contigs[0].reads[5].ds.dye, "")
        self.assertEqual(record.contigs[0].reads[5].ds.template, "")
        self.assertEqual(record.contigs[0].reads[5].ds.direction, "")
        self.assertIsNone(record.contigs[0].reads[5].rt)
        self.assertIsNone(record.contigs[0].reads[5].wr)

        self.assertEqual(record.contigs[0].reads[6].rd.name, "K26-572c")
        self.assertEqual(record.contigs[0].reads[6].rd.padded_bases, 594)
        self.assertEqual(record.contigs[0].reads[6].rd.info_items, 0)
        self.assertEqual(record.contigs[0].reads[6].rd.read_tags, 0)
        center = len(record.contigs[0].reads[6].rd.sequence) // 2
        self.assertEqual(record.contigs[0].reads[6].rd.sequence[:10], "agccccgggc")
        self.assertEqual(
            record.contigs[0].reads[6].rd.sequence[center - 5 : center + 5],
            "ggatcACATA",
        )
        self.assertEqual(record.contigs[0].reads[6].rd.sequence[-10:], "aatagtaaca")
        self.assertEqual(record.contigs[0].reads[6].qa.qual_clipping_start, 249)
        self.assertEqual(record.contigs[0].reads[6].qa.qual_clipping_end, 584)
        self.assertEqual(record.contigs[0].reads[6].qa.align_clipping_start, 1)
        self.assertEqual(record.contigs[0].reads[6].qa.align_clipping_end, 586)
        self.assertEqual(record.contigs[0].reads[6].ds.chromat_file, "K26-572c")
        self.assertEqual(record.contigs[0].reads[6].ds.phd_file, "K26-572c.phd.1")
        self.assertEqual(record.contigs[0].reads[6].ds.time, "Thu Sep 12 15:42:34 1996")
        self.assertEqual(record.contigs[0].reads[6].ds.chem, "")
        self.assertEqual(record.contigs[0].reads[6].ds.dye, "")
        self.assertEqual(record.contigs[0].reads[6].ds.template, "")
        self.assertEqual(record.contigs[0].reads[6].ds.direction, "")
        self.assertIsNone(record.contigs[0].reads[6].rt)
        self.assertIsNone(record.contigs[0].reads[6].wr)

        self.assertEqual(record.contigs[0].reads[7].rd.name, "K26-766c")
        self.assertEqual(record.contigs[0].reads[7].rd.padded_bases, 603)
        self.assertEqual(record.contigs[0].reads[7].rd.info_items, 0)
        self.assertEqual(record.contigs[0].reads[7].rd.read_tags, 0)
        center = len(record.contigs[0].reads[7].rd.sequence) // 2
        self.assertEqual(record.contigs[0].reads[7].rd.sequence[:10], "gaataattgg")
        self.assertEqual(
            record.contigs[0].reads[7].rd.sequence[center - 5 : center + 5],
            "TggCCCATCT",
        )
        self.assertEqual(record.contigs[0].reads[7].rd.sequence[-10:], "gaaccacacg")
        self.assertEqual(record.contigs[0].reads[7].qa.qual_clipping_start, 240)
        self.assertEqual(record.contigs[0].reads[7].qa.qual_clipping_end, 584)
        self.assertEqual(record.contigs[0].reads[7].qa.align_clipping_start, 126)
        self.assertEqual(record.contigs[0].reads[7].qa.align_clipping_end, 583)
        self.assertEqual(record.contigs[0].reads[7].ds.chromat_file, "K26-766c")
        self.assertEqual(record.contigs[0].reads[7].ds.phd_file, "K26-766c.phd.1")
        self.assertEqual(record.contigs[0].reads[7].ds.time, "Thu Sep 12 15:42:35 1996")
        self.assertEqual(record.contigs[0].reads[7].ds.chem, "")
        self.assertEqual(record.contigs[0].reads[7].ds.dye, "")
        self.assertEqual(record.contigs[0].reads[7].ds.template, "")
        self.assertEqual(record.contigs[0].reads[7].ds.direction, "")
        self.assertIsNone(record.contigs[0].reads[7].rt)
        self.assertIsNone(record.contigs[0].reads[7].wr)

    def test_check_record_parser(self):
        """Test to check that record parser parses each contig into a record."""
        contigs = Ace.parse(self.handle)

        # First (and only) contig
        contig = next(contigs)

        self.assertEqual(len(contig.reads), 8)
        self.assertEqual(contig.name, "Contig1")
        self.assertEqual(contig.nbases, 1475)
        self.assertEqual(contig.nreads, 8)
        self.assertEqual(contig.nsegments, 156)
        self.assertEqual(contig.uorc, "U")
        center = len(contig.sequence) // 2
        self.assertEqual(contig.sequence[:10], "agccccgggc")
        self.assertEqual(contig.sequence[center - 5 : center + 5], "CTTCCCCAGG")
        self.assertEqual(contig.sequence[-10:], "gttgggtttg")
        center = len(contig.quality) // 2
        self.assertEqual(contig.quality[:10], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(
            contig.quality[center - 5 : center + 5],
            [90, 90, 90, 90, 90, 90, 90, 90, 89, 89],
        )
        self.assertEqual(contig.quality[-10:], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(len(contig.af), 8)
        self.assertEqual(len(contig.bs), 156)
        self.assertEqual(contig.af[4].name, "K26-291s")
        self.assertEqual(contig.af[4].coru, "U")
        self.assertEqual(contig.af[4].padded_start, 828)
        self.assertEqual(contig.af[7].name, "K26-766c")
        self.assertEqual(contig.af[7].coru, "C")
        self.assertEqual(contig.af[7].padded_start, 408)
        self.assertEqual(contig.bs[78].name, "K26-394c")
        self.assertEqual(contig.bs[78].padded_start, 987)
        self.assertEqual(contig.bs[78].padded_end, 987)
        self.assertEqual(contig.bs[155].name, "K26-822c")
        self.assertEqual(contig.bs[155].padded_start, 1303)
        self.assertEqual(contig.bs[155].padded_end, 1475)
        self.assertEqual(len(contig.ct), 3)
        self.assertEqual(contig.ct[0].name, "Contig1")
        self.assertEqual(contig.ct[0].tag_type, "repeat")
        self.assertEqual(contig.ct[0].program, "consed")
        self.assertEqual(contig.ct[0].padded_start, 976)
        self.assertEqual(contig.ct[0].padded_end, 986)
        self.assertEqual(contig.ct[0].date, "971218:180623")
        self.assertEqual(contig.ct[0].info, [])
        self.assertEqual(contig.ct[1].name, "Contig1")
        self.assertEqual(contig.ct[1].tag_type, "comment")
        self.assertEqual(contig.ct[1].program, "consed")
        self.assertEqual(contig.ct[1].padded_start, 996)
        self.assertEqual(contig.ct[1].padded_end, 1007)
        self.assertEqual(contig.ct[1].date, "971218:180623")
        self.assertEqual(
            contig.ct[1].info,
            ["This is line 1 of a comment", "There may be any number of lines"],
        )
        self.assertEqual(contig.ct[2].name, "Contig1")
        self.assertEqual(contig.ct[2].tag_type, "oligo")
        self.assertEqual(contig.ct[2].program, "consed")
        self.assertEqual(contig.ct[2].padded_start, 963)
        self.assertEqual(contig.ct[2].padded_end, 987)
        self.assertEqual(contig.ct[2].date, "971218:180623")
        self.assertEqual(
            contig.ct[2].info,
            ["standard.1 acataagacattctaaatttttact 50 U", "seq from clone"],
        )
        self.assertEqual(len(contig.wa), 1)
        self.assertEqual(contig.wa[0].tag_type, "phrap_params")
        self.assertEqual(contig.wa[0].program, "phrap")
        self.assertEqual(contig.wa[0].date, "990621:161947")
        self.assertEqual(
            contig.wa[0].info,
            [
                "/usr/local/genome/bin/phrap standard.fasta.screen -new_ace -view",
                "phrap version 0.990319",
            ],
        )

        self.assertEqual(len(contig.reads), 8)

        self.assertEqual(contig.reads[0].rd.name, "K26-217c")
        self.assertEqual(contig.reads[0].rd.padded_bases, 563)
        self.assertEqual(contig.reads[0].rd.info_items, 0)
        self.assertEqual(contig.reads[0].rd.read_tags, 0)
        center = len(contig.reads[0].rd.sequence) // 2
        self.assertEqual(contig.reads[0].rd.sequence[:10], "tcccCgtgag")
        self.assertEqual(
            contig.reads[0].rd.sequence[center - 5 : center + 5], "CTCCTGcctg"
        )
        self.assertEqual(contig.reads[0].rd.sequence[-10:], "ggcccccctc")
        self.assertEqual(contig.reads[0].qa.qual_clipping_start, 19)
        self.assertEqual(contig.reads[0].qa.qual_clipping_end, 349)
        self.assertEqual(contig.reads[0].qa.align_clipping_start, 19)
        self.assertEqual(contig.reads[0].qa.align_clipping_end, 424)
        self.assertEqual(contig.reads[0].ds.chromat_file, "K26-217c")
        self.assertEqual(contig.reads[0].ds.phd_file, "K26-217c.phd.1")
        self.assertEqual(contig.reads[0].ds.time, "Thu Sep 12 15:42:38 1996")
        self.assertEqual(contig.reads[0].ds.chem, "")
        self.assertEqual(contig.reads[0].ds.dye, "")
        self.assertEqual(contig.reads[0].ds.template, "")
        self.assertEqual(contig.reads[0].ds.direction, "")
        self.assertIsNone(contig.reads[0].rt)
        self.assertIsNone(contig.reads[0].wr)

        self.assertEqual(contig.reads[1].rd.name, "K26-526t")
        self.assertEqual(contig.reads[1].rd.padded_bases, 687)
        self.assertEqual(contig.reads[1].rd.info_items, 0)
        self.assertEqual(contig.reads[1].rd.read_tags, 0)
        center = len(contig.reads[1].rd.sequence) // 2
        self.assertEqual(contig.reads[1].rd.sequence[:10], "ccgtcctgag")
        self.assertEqual(
            contig.reads[1].rd.sequence[center - 5 : center + 5], "cacagcccT*"
        )
        self.assertEqual(contig.reads[1].rd.sequence[-10:], "Ttttgtttta")
        self.assertEqual(contig.reads[1].qa.qual_clipping_start, 12)
        self.assertEqual(contig.reads[1].qa.qual_clipping_end, 353)
        self.assertEqual(contig.reads[1].qa.align_clipping_start, 9)
        self.assertEqual(contig.reads[1].qa.align_clipping_end, 572)
        self.assertEqual(contig.reads[1].ds.chromat_file, "K26-526t")
        self.assertEqual(contig.reads[1].ds.phd_file, "K26-526t.phd.1")
        self.assertEqual(contig.reads[1].ds.time, "Thu Sep 12 15:42:33 1996")
        self.assertEqual(contig.reads[1].ds.chem, "")
        self.assertEqual(contig.reads[1].ds.dye, "")
        self.assertEqual(contig.reads[1].ds.template, "")
        self.assertEqual(contig.reads[1].ds.direction, "")
        self.assertIsNone(contig.reads[1].rt)
        self.assertIsNone(contig.reads[1].wr)

        self.assertEqual(contig.reads[2].rd.name, "K26-961c")
        self.assertEqual(contig.reads[2].rd.padded_bases, 517)
        self.assertEqual(contig.reads[2].rd.info_items, 0)
        self.assertEqual(contig.reads[2].rd.read_tags, 0)
        center = len(contig.reads[2].rd.sequence) // 2
        self.assertEqual(contig.reads[2].rd.sequence[:10], "aatattaccg")
        self.assertEqual(
            contig.reads[2].rd.sequence[center - 5 : center + 5], "CAGATGGGTT"
        )
        self.assertEqual(contig.reads[2].rd.sequence[-10:], "ctattcaggg")
        self.assertEqual(contig.reads[2].qa.qual_clipping_start, 20)
        self.assertEqual(contig.reads[2].qa.qual_clipping_end, 415)
        self.assertEqual(contig.reads[2].qa.align_clipping_start, 26)
        self.assertEqual(contig.reads[2].qa.align_clipping_end, 514)
        self.assertEqual(contig.reads[2].ds.chromat_file, "K26-961c")
        self.assertEqual(contig.reads[2].ds.phd_file, "K26-961c.phd.1")
        self.assertEqual(contig.reads[2].ds.time, "Thu Sep 12 15:42:37 1996")
        self.assertEqual(contig.reads[2].ds.chem, "")
        self.assertEqual(contig.reads[2].ds.dye, "")
        self.assertEqual(contig.reads[2].ds.template, "")
        self.assertEqual(contig.reads[2].ds.direction, "")
        self.assertIsNone(contig.reads[2].rt)
        self.assertIsNone(contig.reads[2].wr)

        self.assertEqual(contig.reads[3].rd.name, "K26-394c")
        self.assertEqual(contig.reads[3].rd.padded_bases, 628)
        self.assertEqual(contig.reads[3].rd.info_items, 0)
        self.assertEqual(contig.reads[3].rd.read_tags, 0)
        center = len(contig.reads[3].rd.sequence) // 2
        self.assertEqual(contig.reads[3].rd.sequence[:10], "ctgcgtatcg")
        self.assertEqual(
            contig.reads[3].rd.sequence[center - 5 : center + 5], "AGGATTGCTT"
        )
        self.assertEqual(contig.reads[3].rd.sequence[-10:], "aaccctgggt")
        self.assertEqual(contig.reads[3].qa.qual_clipping_start, 18)
        self.assertEqual(contig.reads[3].qa.qual_clipping_end, 368)
        self.assertEqual(contig.reads[3].qa.align_clipping_start, 11)
        self.assertEqual(contig.reads[3].qa.align_clipping_end, 502)
        self.assertEqual(contig.reads[3].ds.chromat_file, "K26-394c")
        self.assertEqual(contig.reads[3].ds.phd_file, "K26-394c.phd.1")
        self.assertEqual(contig.reads[3].ds.time, "Thu Sep 12 15:42:32 1996")
        self.assertEqual(contig.reads[3].ds.chem, "")
        self.assertEqual(contig.reads[3].ds.dye, "")
        self.assertEqual(contig.reads[3].ds.template, "")
        self.assertEqual(contig.reads[3].ds.direction, "")
        self.assertIsNone(contig.reads[3].rt)
        self.assertIsNone(contig.reads[3].wr)

        self.assertEqual(contig.reads[4].rd.name, "K26-291s")
        self.assertEqual(contig.reads[4].rd.padded_bases, 556)
        self.assertEqual(contig.reads[4].rd.info_items, 0)
        self.assertEqual(contig.reads[4].rd.read_tags, 0)
        center = len(contig.reads[4].rd.sequence) // 2
        self.assertEqual(contig.reads[4].rd.sequence[:10], "gaggatcgct")
        self.assertEqual(
            contig.reads[4].rd.sequence[center - 5 : center + 5], "GTgcgaggat"
        )
        self.assertEqual(contig.reads[4].rd.sequence[-10:], "caggcagatg")
        self.assertEqual(contig.reads[4].qa.qual_clipping_start, 11)
        self.assertEqual(contig.reads[4].qa.qual_clipping_end, 373)
        self.assertEqual(contig.reads[4].qa.align_clipping_start, 11)
        self.assertEqual(contig.reads[4].qa.align_clipping_end, 476)
        self.assertEqual(contig.reads[4].ds.chromat_file, "K26-291s")
        self.assertEqual(contig.reads[4].ds.phd_file, "K26-291s.phd.1")
        self.assertEqual(contig.reads[4].ds.time, "Thu Sep 12 15:42:31 1996")
        self.assertEqual(contig.reads[4].ds.chem, "")
        self.assertEqual(contig.reads[4].ds.dye, "")
        self.assertEqual(contig.reads[4].ds.template, "")
        self.assertEqual(contig.reads[4].ds.direction, "")
        self.assertIsNone(contig.reads[4].rt)
        self.assertIsNone(contig.reads[4].wr)

        self.assertEqual(contig.reads[5].rd.name, "K26-822c")
        self.assertEqual(contig.reads[5].rd.padded_bases, 593)
        self.assertEqual(contig.reads[5].rd.info_items, 0)
        self.assertEqual(contig.reads[5].rd.read_tags, 0)
        center = len(contig.reads[5].rd.sequence) // 2
        self.assertEqual(contig.reads[5].rd.sequence[:10], "ggggatccg*")
        self.assertEqual(
            contig.reads[5].rd.sequence[center - 5 : center + 5], "GCaAgacCCt"
        )
        self.assertEqual(contig.reads[5].rd.sequence[-10:], "gttgggtttg")

        self.assertEqual(contig.reads[5].qa.qual_clipping_start, 25)
        self.assertEqual(contig.reads[5].qa.qual_clipping_end, 333)
        self.assertEqual(contig.reads[5].qa.align_clipping_start, 16)
        self.assertEqual(contig.reads[5].qa.align_clipping_end, 593)
        self.assertEqual(contig.reads[5].ds.chromat_file, "K26-822c")
        self.assertEqual(contig.reads[5].ds.phd_file, "K26-822c.phd.1")
        self.assertEqual(contig.reads[5].ds.time, "Thu Sep 12 15:42:36 1996")
        self.assertEqual(contig.reads[5].ds.chem, "")
        self.assertEqual(contig.reads[5].ds.dye, "")
        self.assertEqual(contig.reads[5].ds.template, "")
        self.assertEqual(contig.reads[5].ds.direction, "")
        self.assertIsNone(contig.reads[5].rt)
        self.assertIsNone(contig.reads[5].wr)

        self.assertEqual(contig.reads[6].rd.name, "K26-572c")
        self.assertEqual(contig.reads[6].rd.padded_bases, 594)
        self.assertEqual(contig.reads[6].rd.info_items, 0)
        self.assertEqual(contig.reads[6].rd.read_tags, 0)
        center = len(contig.reads[6].rd.sequence) // 2
        self.assertEqual(contig.reads[6].rd.sequence[:10], "agccccgggc")
        self.assertEqual(
            contig.reads[6].rd.sequence[center - 5 : center + 5], "ggatcACATA"
        )
        self.assertEqual(contig.reads[6].rd.sequence[-10:], "aatagtaaca")
        self.assertEqual(contig.reads[6].qa.qual_clipping_start, 249)
        self.assertEqual(contig.reads[6].qa.qual_clipping_end, 584)
        self.assertEqual(contig.reads[6].qa.align_clipping_start, 1)
        self.assertEqual(contig.reads[6].qa.align_clipping_end, 586)
        self.assertEqual(contig.reads[6].ds.chromat_file, "K26-572c")
        self.assertEqual(contig.reads[6].ds.phd_file, "K26-572c.phd.1")
        self.assertEqual(contig.reads[6].ds.time, "Thu Sep 12 15:42:34 1996")
        self.assertEqual(contig.reads[6].ds.chem, "")
        self.assertEqual(contig.reads[6].ds.dye, "")
        self.assertEqual(contig.reads[6].ds.template, "")
        self.assertEqual(contig.reads[6].ds.direction, "")
        self.assertIsNone(contig.reads[6].rt)
        self.assertIsNone(contig.reads[6].wr)

        self.assertEqual(contig.reads[7].rd.name, "K26-766c")
        self.assertEqual(contig.reads[7].rd.padded_bases, 603)
        self.assertEqual(contig.reads[7].rd.info_items, 0)
        self.assertEqual(contig.reads[7].rd.read_tags, 0)
        center = len(contig.reads[7].rd.sequence) // 2
        self.assertEqual(contig.reads[7].rd.sequence[:10], "gaataattgg")
        self.assertEqual(
            contig.reads[7].rd.sequence[center - 5 : center + 5], "TggCCCATCT"
        )
        self.assertEqual(contig.reads[7].rd.sequence[-10:], "gaaccacacg")
        self.assertEqual(contig.reads[7].qa.qual_clipping_start, 240)
        self.assertEqual(contig.reads[7].qa.qual_clipping_end, 584)
        self.assertEqual(contig.reads[7].qa.align_clipping_start, 126)
        self.assertEqual(contig.reads[7].qa.align_clipping_end, 583)
        self.assertEqual(contig.reads[7].ds.chromat_file, "K26-766c")
        self.assertEqual(contig.reads[7].ds.phd_file, "K26-766c.phd.1")
        self.assertEqual(contig.reads[7].ds.time, "Thu Sep 12 15:42:35 1996")
        self.assertEqual(contig.reads[7].ds.chem, "")
        self.assertEqual(contig.reads[7].ds.dye, "")
        self.assertEqual(contig.reads[7].ds.template, "")
        self.assertEqual(contig.reads[7].ds.direction, "")
        self.assertIsNone(contig.reads[7].rt)
        self.assertIsNone(contig.reads[7].wr)

        # Make sure there are no more contigs
        self.assertRaises(StopIteration, next, contigs)


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner)
