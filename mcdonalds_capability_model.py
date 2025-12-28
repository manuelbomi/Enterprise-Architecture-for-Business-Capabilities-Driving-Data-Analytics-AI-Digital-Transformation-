import matplotlib.pyplot as plt

capabilities = ["Data Governance", "ML Platform", "Real-Time Analytics", "MLOps"]
maturity = [2, 3, 4, 2]
impact = [5, 4, 5, 5]

plt.scatter(maturity, impact)
for i, cap in enumerate(capabilities):
    plt.text(maturity[i]+0.02, impact[i], cap)

plt.xlabel("Capability Maturity")
plt.ylabel("Business Impact")
plt.title("Capability Investment Prioritization")
plt.show()
