# Load packages to be needed
import collections
import random
import tensorflow as tf
import argparse
import tokenization

class TrainingInstance:
    """A single raiing instance (sentence pair)"""

    def __init__(self, tokens, segment_ids, masked_lm_positions, masked_lm_labels, is_random_next):
        self.tokens = tokens
        self.segment_ids = segment_ids
        self.is_random_next = is_random_next
        self.masked_lm_positions = masked_lm_positions
        self.masked_lm_labels = masked_lm_labels

    def __str__(self):
        s = ""
        s += "token: %s\n" % (" ".join([tokenization.printable_text(x) for x in self.tokens]))
        s += "segment_ids: %s\n" % (" ".join([str(x) for x in self.segment_ids]))
        s += "is_random_next: %s\n" % self.is_random_next
        s += "masked_lm_positions: %s\n" % (" ".join([str(x) for x in self.masked_lm_positions]))
        s += "masked_lm_labels: %s\n" % (" ".join([tokenization.printable_text(x) for x in self.masked_lm_labels]))
        s += "\n"
        return s

    def __repr__(self):
        return str(self)

def write_instance_to_example_files(instances, )



if __name__ == "__main__":
    parser = argparse.ArgumentParser("Create pretraining data")
    
    # parser.add_argument("--input_file", type=str)
    # parser.add_argument("--output_file", type=str)
    # parser.add_argument("--vocab_file", type=str)
    # parser.add_argument("--do_lower_case", type=bool, default=True) # True : 전부 소문자로, False : 대, 소문자 구분
    # parser.add_argument("--max_seq_length", type=int, default=128) # Sequence lenght 를 제한
    # parser.add_argument("--max_predictions_per_seq", type=int, default=20) # [MASK] token 의 최대 개수
    # parser.add_argument("--random_seed", type=int, default=12345)
    # parser.add_argument("--dupe_factor", type=int, default=10, \
    #     help="Number of times to duplicate the input data (with different masks).")
    # parser.add_argument("--masked_lm_prob", type=float, default=0.15, \
    #     help="Masked LM probability")
    # parser.add_argument("--short_seq_prob", type=float, default=0.1, \
    #     help="Probability of creating sequences which are shorter than the maximum length")

    # args = parser.parse_args()
    
    t = TrainingInstance()
    print(str(t), "\n")
    print(t)
    




