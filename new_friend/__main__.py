from .new_friend import train, run
import getopt, sys


def usage():
    print(
        """Usage:
train:
new-friend train --data data_directory/ --out my_saved_model.p

test:
new-friend run --model my_saved_model.p --dry-run

run:
new-friend run --model my_saved_model.p --channel general --token mytoken1234"""
    )


def process_run(args):
    try:
        opts, args = getopt.getopt(
            args, "hc:t:m:d", ["help", "channel=", "token=", "model=", "dry-run"]
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
        elif o in ("-t", "--token"):
            kwargs["token"] = a
        elif o in ("-d", "--dry-run"):
            kwargs["dry_run"] = True
        else:
            assert False, "unhandled option"
    run(**kwargs)


def process_train(args):
    try:
        opts, args = getopt.getopt(args, "hd:o:", ["help", "data=", "out="])
    except getopt.GetoptError as err:
        usage()
        sys.exit(2)
    kwargs = {}
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-d", "--data"):
            kwargs["data_path"] = a
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