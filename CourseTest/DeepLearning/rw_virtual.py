from random_walks import RandomWalk
import matplotlib.pyplot as plt


while True:
    walker = RandomWalk()
    walker.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize = (10,6), dpi = 128)
    
    steps = range(walker.num_points)
    ax.scatter(walker.x_values, walker.y_values,
            c = steps, cmap = plt.cm.Blues,edgecolor = 'none', s = 10)

    ax.scatter(0,0, c = 'green',edgecolor = 'none', s = 100)
    ax.scatter(walker.x_values[-1],walker.y_values[-1],c = 'red',edgecolor = 'none',s = 100)

    plt.show()
    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break
