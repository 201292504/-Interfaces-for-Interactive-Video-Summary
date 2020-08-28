import os
import time, json
import qvsumm
from qvsumm.utils_func import preprocess_video
from qvsumm.shells import *

debug = False

COMMAND_FILEPATH = 'command.txt'
RESULT_FILEPATH = 'result.txt'

if not debug:
    relscore_function = qvsumm.get_QAR_function()
    w2vmodel = qvsumm.get_word2vec_function()

print 'Model loaded...'
videoURL = None


def export_to_result(msg):
    print 'EXPORT:' + msg
    with open(RESULT_FILEPATH, 'w') as f:
        f.write(msg)


def query_summary(query='upload'):
    if debug:
        export_to_result('Preprocessing Video, wait it done...')
        time.sleep(2)
        export_to_result('Getting relatescores, wait it done...')
        time.sleep(2)
        export_to_result('Getting objectives, wait it done...')
        time.sleep(2)
        relscores = [0.111454656465, 0.22256567567, 0.333567567575, 0.444567575757, 0.555675657, 0.6666575676575, 0.8001567575675, 0.3412121212, .945353543, .6234324242]
        relscores = list(sorted(relscores, reverse=True))
        selected_elements = [0, 2, 1, 3, 5, 8, 6, 4, 5, 9]
        results = [[os.path.abspath("videos/frames/" + str(i) + ".png"), relscores[i]] \
                   for i in selected_elements[:10]]
        export_to_result('RESULT:' + json.dumps(results))
        time.sleep(2)
        return

    export_to_result('Preprocessing Video, wait it done...')
    imagenames = preprocess_video(query, videoURL)
    export_to_result('Getting relatescores, wait it done...')
    relscores, intscores = qvsumm.get_rel_Q_scores(relscore_function, w2vmodel, query, imagenames)
    K = 10
    export_to_result('Doing summary, wait it done...')
    S1 = qvsumm.shells.Summ(query, imagenames, relscores, intscores)
    S1.budget = K
    export_to_result('Getting objectives, wait it done...')
    objectives = [quality_shell(S1), similarity_shell(S1), diversity_shell(S1), ex.representativeness_shell(S1)]
    weights = [0.00963344, 0.45267703, 0.43680236, 0.10088718]
    export_to_result('Selecting elements, wait it done...')
    selected_elements, score, _ = gm_submodular.lazy_greedy_maximize(S1, weights, objectives, budget=K, randomize=True)
    results = [[os.path.abspath("videos/frames/" + str(i) + ".png"), relscores[i]] for i in selected_elements[:K]]
    export_to_result('RESULT:' + json.dumps(results))


# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
#
# plt.figure(figsize=(60, 10))
# for enum, i in enumerate(selected_elements[0:K]):
#     if enum == 3:
#         plt.title("Query: " + str(query), fontsize=70)
#     plt.subplot(1, K, enum + 1)
#     plt.imshow(mpimg.imread("videos/frames/" + str(i) + ".png"))
#     plt.axis('off')
#     plt.annotate(str(relscores[i]), xy=(1, 0), xycoords='axes fraction', fontsize=10,
#                  horizontalalignment='right', verticalalignment='bottom', color='green')
# plt.show()


class Client:
    def __init__(self):
        self.timestamp_now = self.parse_command()[0]

    def start_listening(self):
        while True:
            ts, cmd = self.parse_command()
            if ts == self.timestamp_now:
                time.sleep(1)
                continue
            print 'Begin a job: %s....' % cmd
            self.timestamp_now = ts
            query_summary(cmd)

    def parse_command(self):
        return open(COMMAND_FILEPATH, 'r').read().split('#')


# pass
Client().start_listening()
