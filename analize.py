import getopt
import sys

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def usage():
    name = sys.argv[0]
    print "Usage: python " + name + " -i <path to image> [options]"
    print "Options: "
    print "-h, help"
    print "-i, input picture"
    print "-a, averaging\n\tAverage intensity of the given number of adjacent slices"
    print "-r, resolution\n\tSet the tick resolution on axis x"
    print "-s, speed\n\tSet the simulation speed"
    print "-b, background noise\n\tSet the given value as miniumum at axis y"
    print "-m, max value with no scaling\n\tIf the highest value in data exceed the given value then scale the y axis"
    print "-p, picture mode\n\tTake the single shot at given y"


def main(filename, slices_to_average, x_ticks_resolution, px_per_step, noise_threshhold, max_val_threshold, slc):
    def get_slice(slice):
        return [sum(x) for x in arr[slice]]

    def get_smooth_slice(slice):
        to_slice = [(slice + k) %
                    Y for k in range(-slices_to_average, slices_to_average + 1)]
        slices = [get_slice(x) for x in to_slice]
        return [sum(x) / (2 * slices_to_average + 1) for x in zip(*slices)]

    def single_shot(slc):
        data = get_smooth_slice(slc)
        plt.plot(data)

        plt.grid(True)
        axes = plt.gca()
        axes.set_xlim([0, X])
        axes.xaxis.set_ticks(np.arange(0, X, x_ticks_resolution))
        axes.set_ylim([noise_threshhold, max(max_val_threshold, max(data))])
        plt.title("y: " + str(slc) + "px")
        plt.show()

    img = Image.open(filename)
    arr = np.array(img)

    X = len(arr[0])
    Y = len(arr)

    x = range(len(arr[0]))
    y = get_slice(0)

    if slc != -1:
        single_shot(slc)
        sys.exit(0)

    plt.ion()

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.grid(True)
    ax.set_xlabel("x [px]")
    ax.set_ylabel("Intensity [a.u.]")
    # Returns a tuple of line objects, thus the comma
    line1, = ax.plot(x, y, 'r-')

    axes = plt.gca()
    axes.set_xlim([0, X])
    axes.xaxis.set_ticks(np.arange(0, X, x_ticks_resolution))

    for slice in range(0, len(arr), px_per_step):
        data = get_smooth_slice(slice)
        axes.set_ylim([noise_threshhold, max(max_val_threshold, max(data))])
        plt.title("y: " + str(slice) + "px")

        line1.set_ydata(data)
        fig.canvas.draw()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        sys.exit(2)

    try:
        opts, args = getopt.getopt(
            sys.argv[1:], "hi:a:r:s:b:m:p:", ["help", "input", "averaging", "resolution", "speed", "background", "minimum-y", "picture"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    filename = ""
    slices_to_average = 5
    x_ticks_resolution = 100
    px_per_step = 10
    noise_threshhold = 40
    max_val_threshold = 140
    slc = -1

    for o, a in opts:
        if o == "-h":
            usage()
            sys.exit()
        elif o in ("-i", "--input"):
            filename = a
        elif o in ("-a", "--averaging"):
            slices_to_average = int(a)
        elif o in ("-r", "--resolution"):
            x_ticks_resolution = int(a)
        elif o in ("-s", "--speed"):
            px_per_step = int(a)
        elif o in ("-b", "--noise-threshold"):
            noise_threshhold = int(a)
        elif o in ("-m", "--minimum-y"):
            max_val_threshold = int(a)
        elif o in ("-p", "--picture"):
            slc = int(a)
        else:
            assert False, "unhandled option"

    main(filename, slices_to_average, x_ticks_resolution,
         px_per_step, noise_threshhold, max_val_threshold, slc)
