from plot_definitions import *

df_evolution = pd.read_csv(dat_dir+"sfd_evolution.csv")

# Plot settings
lw      = 2.5
fscale  = 2.0
fsize   = 22
sns.set_style("whitegrid")
sns.set(style="ticks", font_scale=fscale)

imf = "powerlaw"
ls  = "-"

fig  = plt.subplots(figsize=(11,11))
grid = plt.GridSpec(4, 1, wspace=0.0, hspace=0.1) #
ax1  = plt.subplot(grid[0:2, 0])
ax2  = plt.subplot(grid[2:4, 0], sharex=ax1)


# ax1.annotate(r'Carbonaceous reservoir (CC)', xy=(1.0, 0.40), va="center", ha="right", fontsize=fsize-6, color=qblue, transform=ax1.transAxes)
# ax1.annotate(r'Non-carbonaceous reservoir (NC)', xy=(0.65, 0.25), va="center", ha="right", fontsize=fsize-6, color=qred, transform=ax1.transAxes)

############# CORE FORMATION AGES

# ## Calc error propagated mean age
# # --> pip install uncertainties
# # https://pypi.org/project/uncertainties/
# import uncertainties
# from uncertainties import ufloat

# NC_irons = np.array([ufloat(0.3, 0.5),  # IC
#                      ufloat(0.8, 0.5),  # IIAB
#                      ufloat(1.2, 0.5),  # IIIAB
#                      ufloat(1.5, 0.6),  # IVA
#                      ufloat(1.8, 0.7)]) # IIIE
#                      # ufloat(6.0, 0.8)]) # IAB

# CC_irons = np.array([ufloat(2.2, 1.1),  # IIF
#                      ufloat(2.3, 0.6),  # IID
#                      ufloat(2.5, 0.7),  # IIF
#                      ufloat(2.6, 1.3),  # IIC
#                      ufloat(2.8, 0.7)]) # IVB

# # Calculate mean and associated error:
# NC_iron_mean = np.mean(NC_irons)
# CC_iron_mean = np.mean(CC_irons)

# print("NC_iron_mean:", NC_iron_mean)
# print("CC_iron_mean:", CC_iron_mean)

# ### Annotate ages as error bars
# lwa            = 1.5
# ages_y_base    = 0.1
# ages_y_base_cc = 0.1
# nc_color_ages  = qred
# cc_color_ages  = qblue

# Values from Sugiura & Fujiya 2014, Desch+ 2018, Kleine+ 2020

# NC IRONS

df = pd.read_csv("../data/pp7/"+"meteorite_data.csv", sep=",", comment="#")
print(df)

# 
for index, row in df.iterrows():
   print(row['class'], row['type'], row['sample'], row['ta'], row['D95mo'])

   if row['class'] == "NC" and row['type'] == "C":
      mc = qred_light
   if row['class'] == "NC" and row['type'] == "A":
      mc = qred
   if row['class'] == "NC" and row['type'] == "I":
      mc = qred_dark
   if row['class'] == "C" and row['type'] == "C":
      mc = qblue_light
   if row['class'] == "C" and row['type'] == "A":
      mc = qblue
   if row['class'] == "C" and row['type'] == "I":
      mc = qblue_dark
   
   
   if row['type'] == "I":
      mt = "^"

   if row['type'] == "A":
      mt = "s"

   if row['type'] == "C":
      mt = "o"

   # Legend labels
   if row['sample'] == "CI":
      label = "C chondrite"
   elif row['sample'] == "Tafassasset":
      label = "C achondrite"
   elif row['sample'] == "IIF":
      label = "C iron"
   elif row['sample'] == "OC":
      label = "NC chondrite"
   elif row['sample'] == "Winonaites":
      label = "NC achondrite"
   elif row['sample'] == "IAB":
      label = "NC iron"
   else:
      label = ""

   # Value
   ax2.plot(float(row['ta']), float(row['D95mo']), ms=10, color=mc, marker=mt, mec="white", zorder=20, label=label)
   # x-error
   ax2.plot([float(row['ta'])-float(row['dta-']),float(row['ta'])+float(row['dta+'])], [float(row['D95mo']),float(row['D95mo'])], color=mc, ls="-", zorder=10)
   # y-error
   ax2.plot([float(row['ta']),float(row['ta'])], [float(row['D95mo'])-float(row['dD95mo']),float(row['D95mo'])+float(row['dD95mo'])], color=mc, ls="-", zorder=10)


# Other timelines

y_min    = 1
y_base   = y_min+0.4
y_delta  = 1
lw       = 25

# CAI formation
ax1.plot([0.0,0.2], [y_base,y_base], color=qgray_light, ls="-", lw=lw, zorder=10, solid_capstyle='butt', alpha=0.99)
ax1.text(0.23, y_base, 'CAIs', color="k", rotation=0, ha="left", va="center", fontsize=fsize-4)
y_base+=y_delta
ax1.plot([0.0,0.3], [y_base,y_base], color=qred_dark, ls="-", lw=lw, zorder=12, solid_capstyle='butt', alpha=0.99)
ax1.plot([0.3,1.8], [y_base,y_base], color=qred, ls="-", lw=lw, zorder=11, solid_capstyle='butt', alpha=0.99)
ax1.plot([0.0,2.2], [y_base,y_base], color=qred_light, ls="-", lw=lw, zorder=10, solid_capstyle='butt', alpha=0.99)
ax1.text(2.25, y_base, 'NC planetesimals', color="k", rotation=0, ha="left", va="center", fontsize=fsize-4, zorder=20)
y_base+=y_delta
ax1.plot([0.8,2.7], [y_base,y_base], color=qred, ls="-", lw=lw, zorder=10, solid_capstyle='butt', alpha=0.99)
ax1.text(2.75, y_base, '50% Mars', color="k", rotation=0, ha="left", va="center", fontsize=fsize-4, zorder=20)
y_base+=y_delta
ax1.plot([1.2,1.6], [y_base,y_base], color=qblue_dark, ls="-", lw=lw, zorder=12, solid_capstyle='butt', alpha=0.99)
ax1.plot([1.6,2.4], [y_base,y_base], color=qblue, ls="-", lw=lw, zorder=11, solid_capstyle='butt', alpha=0.99)
ax1.plot([1.2,4.0], [y_base,y_base], color=qblue_light, ls="-", lw=lw, zorder=10, solid_capstyle='butt', alpha=0.99)
ax1.text(3.2, y_base, 'C planetesimals', color="k", rotation=0, ha="center", va="center", fontsize=fsize-4, zorder=20)
y_base+=y_delta
ax1.plot([0.0,4.0], [y_base,y_base], color=qmagenta_light, ls="-", lw=lw, zorder=10, solid_capstyle='butt', alpha=0.99)
ax1.text(2.0, y_base, 'Chondrules', color="k", rotation=0, ha="center", va="center", fontsize=fsize-4, zorder=20)
y_base+=y_delta
ax1.plot([1.7,4.9], [y_base,y_base], color=qblue_light, ls="-", lw=lw, zorder=10, solid_capstyle='butt', alpha=0.99)
ax1.text(1.65, y_base, 'Comets', color="k", rotation=0, ha="right", va="center", fontsize=fsize-4, zorder=20)
y_base+=y_delta
ax1.plot([4.0,5.0], [y_base,y_base], color=qblue_light, ls="-", lw=lw, zorder=10, solid_capstyle='butt', alpha=0.99)
ax1.text(3.95, y_base, 'CB impact', color="k", rotation=0, ha="right", va="center", fontsize=fsize-4, zorder=20)
y_base+=y_delta

y_max = y_base

# Axes settings

time_ticks  = [ 0.0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5 ]
time_labels = [ str(n) for n in time_ticks ]
# time_labels = [ "0.0", "0.5", "1.0", "1", "1.3", "2", "3", "4", "5" ]

# ax2.set_xscale("symlog", linthreshx=2.0)
# ax2.set_xscale("log")
# ax2.set_yscale("log")

ax1.set_ylim([y_min, y_max-0.3])

ax2.set_ylim(bottom=-42, top=60)

ax2.set_xlim([np.min(time_ticks), np.max(time_ticks)])
ax2.set_xticks(time_ticks)
ax2.set_yticks([-30, -15, 0, 15, 30, 45])
ax2.set_xticklabels(time_labels)

# ax2.set_ylim([0.0001, 1])
# ax2.set_yticks([1e-4, 3e-4, 1e-3, 3e-3, 1e-2, 3e-2, 1e-1, 3e-1, 1])
# ax2.set_yticklabels(["0.01", "0.03", "0.1", "0.3", "1", "3", "10", "30", "100"])

ax2.tick_params(axis="both", labelsize=fsize-2)

ax1.tick_params(axis='x', which='both', bottom=True, top=False, labelbottom=False, colors='black')
ax1.tick_params(axis='y', which='both', bottom=False, top=False, labelbottom=False, colors='white')
ax1.spines['top'].set_color('white')
# ax1.spines['bottom'].set_color('white')
ax1.spines['left'].set_color('white')
ax1.spines['right'].set_color('white')
# ax1.set_facecolor("#f7f7f7")

ax2.set_xlabel(r"Time after CAI formation, $\Delta t_\mathrm{CAI}$ (Myr)", fontsize=fsize+2)
ax2.set_ylabel(r"Isotopic anomaly, $\Delta^{95}$Mo", fontsize=fsize+2)

###### ANNOTATIONS

ax1.text(0.01, 0.96, 'A', color="k", rotation=0, ha="left", va="center", fontsize=fsize+3, transform=ax1.transAxes)
ax1.text(0.05, 0.96, 'Timeline of Solar System accretion', color=qgray_dark, rotation=0, ha="left", va="center", fontsize=fsize-6, transform=ax1.transAxes)
ax2.text(0.01, 0.95, 'B', color="k", rotation=0, ha="left", va="center", fontsize=fsize+3, transform=ax2.transAxes)
ax2.text(0.05, 0.95, 'NC and C planetesimal accretion times', color=qgray_dark, rotation=0, ha="left", va="center", fontsize=fsize-6, transform=ax2.transAxes)

ax2.legend(ncol=3, fontsize=fsize-8, loc=[0.33, 0.02]).set_zorder(102)

sns.despine(ax=ax2, bottom=False, top=True, left=False, right=True)

plt.savefig(fig_dir+"/21_PP7/"+"fig_3.1a"+".pdf", bbox_inches='tight')
# plt.savefig(fig_dir+"fig_4"+".jpg", bbox_inches='tight', dpi=300)
