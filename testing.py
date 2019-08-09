import unittest
#import cypher
import cypher_ck 

class TestCypher(unittest.TestCase):

    def test_One(self):
        pl = "I PLAY WITH"
        # result = cypher.cypher_old(pl)
        result = cypher_ck.cypher_ck(pl)
        self.assertEqual(result , "dqnmzxmdlv")

    def test_Two(self):
            pl = "ADHVVRGTJV FJGDFBJ RIGHRI H RITHER RENGFHN TKHJRTKHEJROG WORT OEW"
            # result = cypher.cypher_old(pl)
            result = cypher_ck.cypher_ck(pl)
            self.assertEqual(result , "tipdxpogdwcabtgcmqtclpdkqmdolxxlofbnoalkmqiolbmquozkumlgxy")
    
    def test_Two(self):
        pl = "ADHVVRGTJV FJGDFBJ RIGHRI H RITHER RENGFHN TKHJRTKHEJROG WORT OEW vakfhsf drewbr uewr ewgruewdgaudgfuas bweurw eurewbtuqerbqeur wbewurwegfw uegruf ewbrewurbfwe urb32truqe bqewruwe br qeurewruqer qeur qev ruqevr qruq"
        # result = cypher.cypher_old(pl)
        result = cypher_ck.cypher_ck(pl)
        self.assertEqual(result , "tipdxpogdwcabtgcmqtclpdkqmdolxxlofbnoalkmqiolbmquozkumlgxwinbnynmpcxeprgxqcxeurgviftptbgstpfxcpsxcpscxgdprlxcpgrqxcfzqqxfbcyrgeusgcxepcxpscgxcpssprccpcxspxceprcpscxsprcsrgrsrbxsprcxprspr")


if __name__ == '__main__':
    unittest.main()