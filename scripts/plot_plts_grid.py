from plot_definitions import *

# Define colormap normalization, labels and ticks
cmap_scale          = "log"
linear_ticks        = [0.001, 0.1, 0.2, 0.3]
linear_ticks_label  = ['Earth', '0.1', '0.2', '0.3']
log_ticks           = [1e-4, 1e-3, 1e-2, 1e-1, 0.3]
log_ticks_label     = ['-4', '-3', '-2', '-1', '-0.5']
if cmap_scale == "log":
    cbar_ticks          = log_ticks
    cbar_ticks_label    = log_ticks_label
    norm = colors.LogNorm(vmin=min(log_ticks), vmax=max(log_ticks)) # log
if cmap_scale == "linear":
    cbar_ticks          = linear_ticks
    cbar_ticks_label    = linear_ticks_label
    norm = colors.Normalize(vmin=min(linear_ticks), vmax=max(linear_ticks)) # linear

fscale  = 3.5
fsize   = 20
sns.set(font_scale=fscale)

sns.axes_style("white")
sns.set_style("ticks")

# Working directories
working_dir = os.getcwd()
dat_dir     = working_dir+"/../data/two_stage/data/planetesimal_evolution/"
fig_dir     = working_dir+"/../figures/"

df = pd.read_csv(dat_dir+"plts_all_data.csv")
RUN_LIST = natsorted(set(df.run.tolist()))

with open(dat_dir+"grid_parameter_space.csv", 'r') as csvfile:

    csvreader = csv.reader(csvfile)
    grid_parameter_space = []
    for row in csvreader:
        grid_parameter_space.append(row)

    rad             = [ float(k) for k in grid_parameter_space[0]]
    tform           = [ float(k) for k in grid_parameter_space[1]]
    sol_frac        = [ float(k) for k in grid_parameter_space[2]]
    liq_frac        = [ float(k) for k in grid_parameter_space[3]]
    hydrous_frac    = [ float(k) for k in grid_parameter_space[4]]
    primitive_frac  = [ float(k) for k in grid_parameter_space[5]]
    n2co2_frac      = [ float(k) for k in grid_parameter_space[6]]
    cocl_frac       = [ float(k) for k in grid_parameter_space[7]]
    h2o_frac        = [ float(k) for k in grid_parameter_space[8]]
    perco_frac      = [ float(k) for k in grid_parameter_space[9]]
    melt1_frac      = [ float(k) for k in grid_parameter_space[10]]
    melt2_frac      = [ float(k) for k in grid_parameter_space[11]]
    Tmax_grid       = [ float(k) for k in grid_parameter_space[12]]
    Tmean_markers   = [ float(k) for k in grid_parameter_space[13]]

rad                 = np.asarray(rad)
tform               = np.asarray(tform)
sol_frac            = np.asarray(sol_frac)
liq_frac            = np.asarray(liq_frac)
hydrous_frac        = np.asarray(hydrous_frac)
primitive_frac      = np.asarray(primitive_frac)
n2co2_frac          = np.asarray(n2co2_frac)
cocl_frac           = np.asarray(cocl_frac)
h2o_frac            = np.asarray(h2o_frac)
perco_frac          = np.asarray(perco_frac)
melt1_frac          = np.asarray(melt1_frac)
melt2_frac          = np.asarray(melt2_frac)
Tmax_grid           = np.asarray(Tmax_grid)
Tmean_markers       = np.asarray(Tmean_markers)

# define grid.
xi = np.linspace(min(rad), max(rad), 100)
yi = np.linspace(min(tform), max(tform), 100)

grid_x, grid_y = np.mgrid[min(rad):max(rad):100j, min(tform):max(tform):100j]

points = np.stack([rad, tform], axis=1)

# https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.griddata.html
zi_sol_frac = scipy.interpolate.griddata(points, sol_frac, (grid_x, grid_y), method='linear', rescale=False)
zi_liq_frac = scipy.interpolate.griddata(points, liq_frac, (grid_x, grid_y), method='linear', rescale=False)
zi_hydrous_frac = scipy.interpolate.griddata(points, hydrous_frac, (grid_x, grid_y), method='linear', rescale=False)
zi_primitive_frac = scipy.interpolate.griddata(points, primitive_frac, (grid_x, grid_y), method='linear', rescale=False)
zi_n2co2_frac = scipy.interpolate.griddata(points, n2co2_frac, (grid_x, grid_y), method='linear', rescale=False)
zi_cocl_frac = scipy.interpolate.griddata(points, cocl_frac, (grid_x, grid_y), method='linear', rescale=False)
zi_h2o_frac = scipy.interpolate.griddata(points, h2o_frac, (grid_x, grid_y), method='linear', rescale=False)
zi_perco_frac = scipy.interpolate.griddata(points, perco_frac, (grid_x, grid_y), method='linear', rescale=False)
zi_melt1_frac = scipy.interpolate.griddata(points, melt1_frac, (grid_x, grid_y), method='linear', rescale=False)
zi_melt2_frac = scipy.interpolate.griddata(points, melt2_frac, (grid_x, grid_y), method='linear', rescale=False)
zi_Tmax_grid = scipy.interpolate.griddata(points, Tmax_grid, (grid_x, grid_y), method='linear', rescale=False)
zi_Tmean_markers = scipy.interpolate.griddata(points, Tmean_markers, (grid_x, grid_y), method='linear', rescale=False)

zi_list = [ "zi_Tmax_grid", "zi_perco_frac" ]

# PLOT SETTINGS
label_font      = 22
tick_font       = 20
annotate_font   = 16
lw              = 10
tw              = 1.5

fig = plt.figure(figsize=(10,10))
ax1 = fig.add_subplot(111)
plt.tight_layout(pad=0.2, w_pad=1, h_pad=0.2)

# divider = make_axes_locatable(ax1)
# cax = divider.append_axes("top", size="4%", pad="2%")
# fig.add_axes(cax, label='a')

# axins1 = inset_axes(ax1,
#                     width="50%",  # width = 50% of parent_bbox width
#                     height="5%",  # height : 5%
#                     loc='lower left')

zi = zi_Tmax_grid

# Colorbar settings
no_color_fields = 255

# cmap = sns.cubehelix_palette(light=1, as_cmap=True)
# cmap = "viridis_r"
# cbar_ticks_labels = [ str(round(round(k,2)*100)) for k in cbar_ticks ]

### Color field loops for smoothing contourf
nloops = 3

for i in range(0, nloops):
    CS = ax1.contourf(grid_x, grid_y, zi, no_color_fields, cmap="magma")#, vmax=cmap_max, vmin=cmap_min)#, extend='max')

# Water
contour_water = ax1.contour(grid_x, grid_y, zi_h2o_frac, [0.1, 0.9], colors=qblue, linewidths=3.0, linestyles=["-", "--"])
# N2/CO2
contour_water = ax1.contour(grid_x, grid_y, zi_n2co2_frac, [0.1, 0.9], colors=qgreen, linewidths=3.0, linestyles=["-", "--"])
# CO
contour_water = ax1.contour(grid_x, grid_y, zi_cocl_frac, [0.1, 0.9], colors=qred, linewidths=3.0, linestyles=["-", "--"])

# cbar = fig.colorbar(CS, cax=axins1, orientation="horizontal", ticks=cbar_ticks)
# cbar.outline.set_edgecolor('black')
# cbar.outline.set_linewidth(1)

# # Scatter plot for individual simulations
# ax1.scatter(rad, tform, marker='o', facecolors='white', edgecolors='black', s=10, zorder=5, lw=1.0, alpha=0.5)

# # Red for Reservoir I
# tform_resI  = np.ma.masked_where((tform > 0.3), tform)
# rad_resI    = np.ma.masked_where((tform > 0.3), rad)
# tform_resI  = np.ma.masked_where((tform < 0.1), tform_resI)
# rad_resI    = np.ma.masked_where((tform < 0.1), rad_resI)
# ax1.scatter(rad_resI, tform_resI, marker='o', facecolors=reds[3], s=25, zorder=5, lw=1.0, alpha=0.99)

# # Blue for Reservoir II
# tform_resII = np.ma.masked_where((tform <= 0.7), tform)
# rad_resII   = np.ma.masked_where((tform <= 0.7), rad)
# ax1.scatter(rad_resII, tform_resII, marker='o', facecolors=blues[3], s=25, zorder=5, lw=1.0, alpha=0.99)

# # Special points for plot B
# rad_B   = np.asarray([ 10., 30., 300. ])
# tform_B = np.asarray([ 0.3, 0.3, 0.3 ])
# print(rad_B, tform_B)
# ax1.scatter(rad_B, tform_B, marker='o', facecolors=qgreen, edgecolors="black", s=120, zorder=6, lw=1.0, alpha=0.99)

# # Special points for plot B
# rad_B   = np.asarray([ 100., 100., 100. ])
# tform_B = np.asarray([ 0.3, 0.72, 1.43 ])
# print(rad_B, tform_B)
# ax1.scatter(rad_B, tform_B, marker='o', facecolors=qmagenta, edgecolors="black", s=120, zorder=6, lw=1.0, alpha=0.99)

# R1_text = ax1.text(9.5, 0.286, 'R1', color=qgreen, rotation=0, fontsize=fsize, ha="right", va="top", zorder=10, bbox=dict(fc='white', ec="white", alpha=0.0, pad=0.1, boxstyle='round'))
# R2_text = ax1.text(28, 0.286, 'R2', color=qgreen, rotation=0, fontsize=fsize, ha="right", va="top", zorder=10, bbox=dict(fc='white', ec="white", alpha=0.0, pad=0.1, boxstyle='round'))
# R3_text = ax1.text(285, 0.286, 'R3', color=qgreen, rotation=0, fontsize=fsize, ha="right", va="top", zorder=10, bbox=dict(fc='white', ec="white", alpha=0.0, pad=0.1, boxstyle='round'))
# T1_text = ax1.text(93, 0.286, 'T1', color=qmagenta, rotation=0, fontsize=fsize, ha="right", va="top", zorder=10, bbox=dict(fc='white', ec="white", alpha=0.0, pad=0.1, boxstyle='round'))
# T2_text = ax1.text(93, 0.68, 'T2', color=qmagenta, rotation=0, fontsize=fsize, ha="right", va="top", zorder=10, bbox=dict(fc='white', ec="white", alpha=0.0, pad=0.1, boxstyle='round'))
# T3_text = ax1.text(93, 1.38, 'T3', color=qmagenta, rotation=0, fontsize=fsize, ha="right", va="top", zorder=10, bbox=dict(fc='white', ec="white", alpha=0.0, pad=0.1, boxstyle='round'))

# ResI_text = ax1.text(1.05, 0.57, 'Reservoir II\nplanetesimals', color=blues[3], rotation=0, fontsize=fsize+1, ha="left", va="center", bbox=dict(fc='white', ec="white", alpha=0.0, pad=0.1, boxstyle='round'), zorder=15)
# nf_text = ax1.text(1.05, 0.36, 'not formed', color="grey", rotation=0, fontsize=fsize-3, ha="left", va="center", alpha=0.8, zorder=15)
# ResII_text = ax1.text(1.05, 0.15, 'Reservoir I\nplanetesimals', color=reds[3], rotation=0, fontsize=fsize+1, ha="left", va="center", bbox=dict(fc='white', ec="white", alpha=0.0, pad=0.1, boxstyle='round'), zorder=15)

# for text in [ R1_text, R2_text, R3_text, T1_text, T2_text, T3_text ]:
#     text.set_path_effects([path_effects.Stroke(linewidth=1.0, foreground='black'),
#                        path_effects.Normal()])

# ax1.text(-0.12, +1.13, 'A', color="k", rotation=0, ha="left", va="top", fontsize=fsize+10, transform=ax1.transAxes, bbox=dict(fc='white', ec="white", alpha=0.01, pad=0.1, boxstyle='round'))

# new_loc = np.logspace(-1,0,9)
# print new_loc, tick_function(new_loc)

# # More colorbar settings
# cbar.set_label(cbar_label, fontsize=fsize+7, labelpad=+20)
# cbar.ax.tick_params(labelsize=fsize) 
# cbar.ax.xaxis.set_label_position('top')
# cbar.ax.xaxis.set_ticks_position('top')
# cbar.ax.set_xticklabels(cbar_ticks_labels)

# Axes settings
ax1.set_xlim(1, 300)
ax1.set_ylim(0.1, 2.0)
ax1.set_xscale("log") 
# ax1.set_yscale("log") 
ax1.set_xticks([1, 2, 3, 5, 7, 10, 20, 30, 50, 100, 200, 300])
ax1.set_xticklabels(["1", "2", "3", "5", "7", "10", "20", "30", "50", "100", "200", "300"], fontsize=fsize)
tform_list_show = np.array([0.0, 0.5, 1.0, 1.5, 2.0])
ax1.set_yticks(tform_list_show)
ax1.set_yticklabels(["0.0", "0.5", "1.0", "1.5", "2.0"], fontsize=fsize)
# ax1.xaxis.tick_bottom()
ax1.xaxis.tick_top()


ax1.tick_params(axis='x', which='both', right='on', top='on', labelsize=fsize, width=tw, color="black", pad=7.)
ax1.tick_params(axis='y', which='both', right='on', top='on', labelsize=fsize, width=tw, color="black", pad=7.)

ax1.set_xlabel(r"Planetesimal radius, $R_{\mathrm{P}}$ (km)", fontsize=fsize)
ax1.set_ylabel(r"Solar System time, $\tau_{\odot}$ (Myr)", fontsize=fsize)
ax1.xaxis.set_label_coords(0.5, +1.11)
# ax1.xaxis.set_label_position('top') 

# plt.gca().axes.get_yaxis().set_visible(False)

plt.gca().invert_yaxis()

# 2nd y-axis: Al-26 from tform (relartive to CAI initial)
def transform_tform_to_al26(t):
    # https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.log.html
    # t = -1.0344*np.log(Al)
    # return [ "%.2f" % z for z in t ]
    Al = 5.25*np.exp(-t/1.03)
    Al = Al/5.25 # normalise to CAIs
    return [ "%.2f" % z for z in Al ]
# Test:
# tform_list  = np.array(natsorted(set(tform)))
# Al26_init   = transform_tform_to_al26(tform_list)
# print(tform_list)
# print(Al26_init)

ax2 = ax1.twinx()
# tform_list_show = np.array([3.0, 0.0])
ax2.set_ylim(ax1.get_ylim())
ax2.set_yticks(tform_list_show)
ax2.set_yticklabels(transform_tform_to_al26(tform_list_show), fontsize=fsize)
ax2.set_ylabel(r"Enrichment level, $^{26}$Al$_{\mathrm{exo}}$/$^{26}$Al$_{\odot}$ (non-dim.)", fontsize=fsize)

# divider = make_axes_locatable(ax2)
# cax = divider.append_axes("top", size="5%", pad="-55%")
# fig.add_axes(cax, label='a')
# cax =  fig.add_axes([0.8, 0.1, 0.03, 0.8]) 
cbar_ticks        = [zi.min(), zi.min()+(zi.max()-zi.min())*0.2, zi.min()+(zi.max()-zi.min())*0.4, zi.min()+(zi.max()-zi.min())*0.6, zi.min()+(zi.max()-zi.min())*0.8, zi.max()]
cbar_ticks        = [ int(round(k)) for k in cbar_ticks ]
cbar_ticks_labels = cbar_ticks
cbar = fig.colorbar(CS, orientation="horizontal", ticks=cbar_ticks, pad=+0.02)
cbar.outline.set_edgecolor('black')
cbar.outline.set_linewidth(1)
cbar_label = r"Maximum temperature, $T_\mathrm{max}$ (K)"
cmap = sns.cubehelix_palette(light=1, as_cmap=True) # "magma", "YlGnBu", "viridis_r"
cbar.set_label(cbar_label, fontsize=fsize+7, labelpad=+20)
cbar.ax.tick_params(labelsize=fsize) 
# cbar.ax.xaxis.set_label_position('top')
# cbar.ax.xaxis.set_ticks_position('top')
# cbar.ax.set_xticklabels(cbar_ticks_labels)

plt.savefig(fig_dir+"fig_plts_grid"+".pdf", bbox_inches='tight')
