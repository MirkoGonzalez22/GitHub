import imageio.v3 as iio

filenames = ['foto1.jpg', 'foto2.jpg']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('team.gif', images, duration = 500, loop = 0)
