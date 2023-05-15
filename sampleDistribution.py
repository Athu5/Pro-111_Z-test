import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import pandas as pd
import random

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].to_list()

population_mean = statistics.mean(data)

st_dv = statistics.stdev(data)
print("Population mean is:{}".format(population_mean))


def random_set_of_means(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["Reading_time"], show_hist=False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0, 100):
        set_of_means = random_set_of_means(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)

    mean = statistics.mean(mean_list)
    print("mean of sampling distribution", mean)

setup()
