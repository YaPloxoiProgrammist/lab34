import numpy as np
from datetime import datetime
import cv2

datetimes = np.genfromtxt('datetimes.csv', delimiter=';', dtype='unicode')
start_datetimes = []
end_datetimes = []
for i in range(datetimes.shape[0]):
    start_datetime_str = datetimes[i][0] + ' ' + datetimes[i][1]
    start_datetimes.append(datetime.strptime(start_datetime_str, '%d.%m.%Y %H:%M'))
    end_datetime_str = datetimes[i][2] + ' ' + datetimes[i][3]
    end_datetimes.append(datetime.strptime(end_datetime_str, '%d.%m.%Y %H:%M'))

dur = np.array([])
for i in range(datetimes.shape[0]):
    dur = np.append(dur, (end_datetimes[i] - start_datetimes[i]).seconds // 3600)

print(dur)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1)
k = 5
ret, label, center = cv2.kmeans(dur, k, None, criteria, 5, cv2.KMEANS_RANDOM_CENTERS)

