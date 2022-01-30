from matplotlib import pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
langs = ["Total No.of Testcases", "Passed", "Failed", "To Do", "Partially Executed", "Not Yet Released", "Blocked"]
students = [470, 137, 20, 237, 4, 31, 41]
ax.pie(students, labels = langs,autopct='%1.5f%%')
plt.show()
