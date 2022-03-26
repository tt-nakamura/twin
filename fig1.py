import matplotlib.pyplot as plt

plt.figure(figsize=(2.5,1))
plt.axis('off')
plt.subplots_adjust(left=0.05, bottom=0.1, right=0.95, top=0.9)
plt.axis([-0.02, 2.22, -0.02, 1.02])
plt.arrow(0,0,2.2,0, head_width=0.03, length_includes_head=True)# x-axis
plt.arrow(0,0,0,1, head_width=0.03, length_includes_head=True)# y-axis
plt.plot([0,1],[0,0.8], 'k')# world line OP
plt.plot([1,2],[0.8,0], 'k')# world line PQ
plt.plot([1,0.6],[0.8,0], 'r--')# simultaneity of OP
plt.plot([2/3,0.4],[1.6/3,0], 'r--')# simultaneity of OP
plt.plot([1/3,0.2],[0.8/3,0], 'r--')# simultaneity of OP
plt.plot([1,1.4],[0.8,0], 'r--')# simultaneity of PQ
plt.plot([4/3,1.6],[1.6/3,0], 'r--')# simultaneity of PQ
plt.plot([5/3,1.8],[0.8/3,0], 'r--')# simultaneity of PQ
plt.text(2.2,0,r'$t$',va='center')
plt.text(0,1,r'$z$',ha='center')
plt.text(0,0,'O',va='top',ha='center')
plt.text(1,0.8,'P',va='bottom',ha='center')
plt.text(2,0,'Q',va='top',ha='center')
plt.text(0.6,0,'R',va='top',ha='center')
plt.text(1.4,0,'S',va='top',ha='center')
plt.savefig('fig1.eps')
plt.show()
