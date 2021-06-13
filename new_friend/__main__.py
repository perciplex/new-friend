from .new_friend import train, run
import getopt, sys


def usage():
    print(
        """Usage:
  new-friend train --out my_saved_model.p
  new-friend run --model my_saved_model.p --token mytoken1234
  new-friend run --channel general --token mytoken1234
    """
    )


def process_run(args):
    try:
        opts, args = getopt.getopt(
            args, "hc:t:m:", ["help", "channel=", "token=", "model=", "train"]
        )
    except getopt.GetoptError as err:
        usage()
        sys.exit(2)
    kwargs = {}
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-c", "--channel"):
            kwargs["channel"] = a
        elif o in ("-m", "--model"):
            kwargs["model_path"] = a
        elif o in ("--token"):
            kwargs["token"] = a
        elif o in ("-t" "--train"):
            kwargs["train"] = True
        else:
            assert False, "unhandled option"
    run(**kwargs)


def process_train(args):
    try:
        opts, args = getopt.getopt(args, "ho:", ["help", "out="])
    except getopt.GetoptError as err:
        usage()
        sys.exit(2)
    kwargs = {}
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-o", "--out"):
            kwargs["output_path"] = a
        else:
            assert False, "unhandled option"
    train(**kwargs)


command = sys.argv[1]
if command == "run":
    process_run(sys.argv[2:])
if command == "train":
    process_train(sys.argv[2:])