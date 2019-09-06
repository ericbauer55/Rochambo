from unittest import TestCase
import topcoder1 as src

class TestRochambo(TestCase):
    z = src.Rochambo()

    def test_wins(self):
        # do all sample cases achieve the same output as the TopCoder sample outputs?
        inputs = ['PS',
                  'PSRRPS',
                  'PSRPSRPRSR',
                  'SRPSRPSPRSPRPSRPSRP',
                  'RPPPRRPSSSRRRSRSPPSSPRRPSRRRRSPPPPSSPSSSSSRSSSRPRR']
        outputs = [1, 3, 7, 16, 18]
        for i in range(len(inputs)):
            self.assertEqual(self.z.wins(inputs[i]), outputs[i])

    def test_beats(self):
        # Logical checks first -- does it evaluate real inputs correctly
        self.assertTrue(src.Rochambo.beats('R', 'S'))
        self.assertTrue(src.Rochambo.beats('P', 'R'))
        self.assertTrue(src.Rochambo.beats('S', 'P'))

        self.assertFalse(src.Rochambo.beats('R', 'R'))
        self.assertFalse(src.Rochambo.beats('P', 'P'))
        self.assertFalse(src.Rochambo.beats('S', 'S'))

        self.assertFalse(src.Rochambo.beats('S', 'R'))
        self.assertFalse(src.Rochambo.beats('R', 'P'))
        self.assertFalse(src.Rochambo.beats('P', 'S'))
        # TODO: Check input types


    def test_generateMoves(self):
        # do all sample cases achieve the same output as the TopCoder sample outputs?
        inputs = ['PS',
                  'PSRRPS',
                  'PSRPSRPRSR']
        outputs = ['RR',
                   'RRPSPR',
                   'RRPSRPSRRS']
        for i in range(len(inputs)):
            self.z.generateMoves(inputs[i])
            self.assertEqual(self.z.y, outputs[i])

