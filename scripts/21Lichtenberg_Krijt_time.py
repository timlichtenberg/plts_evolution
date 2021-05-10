from plot_definitions import *

sns.set_style("whitegrid")
sns.set(style="ticks", font_scale=fscale)

cmap = "YlGnBu"

# READ IN PLANETESIMAL DATA
df = pd.read_csv(dat_dir+"plts_all_data.csv")

RUN_LIST_ALL = natsorted(set(df.run.tolist()))

RUN_LIST       = [ 
                    "r010t000al05250fe01150tmp150",
                    "r100t100al05250fe01150tmp150",   
                    "r100t000al05250fe01150tmp150",               
                    ]

fig = plt.figure(figsize=(10,9))
ax1 = fig.add_subplot(111)

c_counter1 = 0
c_counter2 = 0

rad_palette = sns.color_palette("Set1")

for idx in range(0,9):

    print(idx)

    if idx == 0:
        RUN   = RUN_LIST[0]
        ls    = ":"
        color = qred
        char  = r'CO$_\mathrm{2}$'
        quantity = df[df['run']==RUN].cocl_frac.tolist()
    if idx == 1:
        RUN   = RUN_LIST[1]
        ls    = "--"
        color = qred
        char  = r'CO$_\mathrm{2}$, '
        quantity = df[df['run']==RUN].cocl_frac.tolist()
    if idx == 2:
        RUN   = RUN_LIST[2]
        ls    = "-"
        color = qred
        char  = r'CO$_\mathrm{2}$, '
        quantity = df[df['run']==RUN].cocl_frac.tolist()
    
    if idx == 3:
        RUN   = RUN_LIST[0]
        ls    = ":"
        color = qblue
        char  = r'H$_\mathrm{2}$O'
        quantity = df[df['run']==RUN].h2o_frac.tolist()
        # plt.plot([0], [0], color="white", label=char)
    if idx == 4:
        RUN   = RUN_LIST[1]
        ls    = "--"
        color = qblue
        char  = r'H$_\mathrm{2}$O, '
        quantity = df[df['run']==RUN].h2o_frac.tolist()
    if idx == 5:
        RUN   = RUN_LIST[2]
        ls    = "-"
        color = qblue
        char  = r'H$_\mathrm{2}$O, '
        quantity = df[df['run']==RUN].h2o_frac.tolist()
    
    if idx == 6:
        RUN   = RUN_LIST[0]
        ls    = ":"
        color = qgreen
        char  = r'H$_\mathrm{2}$O'
        quantity = df[df['run']==RUN].n2co2_frac.tolist()
        # plt.plot([0], [0], color="white", label=char)
    if idx == 7:
        RUN   = RUN_LIST[1]
        ls    = "--"
        color = qgreen
        char  = r'H$_\mathrm{2}$O, '
        quantity = df[df['run']==RUN].n2co2_frac.tolist()
    if idx == 8:
        RUN   = RUN_LIST[2]
        ls    = "-"
        color = qgreen
        char  = r'H$_\mathrm{2}$O, '
        quantity = df[df['run']==RUN].n2co2_frac.tolist()

    time = df[df['run']==RUN].time.tolist()

    r_init   = int(float(RUN[1:4]))     # km
    t_form   = float(RUN[5:8])*1e-2     # Myr
    al_init  = round(5.25*np.exp(-t_form/1.03)/5.25,2)   # 26Al relave to CAI value

    tstart_str = str(float(RUN[1:4]))

    # Reset time to after plts formation
    time = [ t-time[0] for t in time ]

    if idx in [0, 1, 2]:
        plt.plot([0], [0], color="black", ls=ls, lw=2.5, label=str(r_init)+" km, "+str(al_init)+r" $^{26}$Al$_\odot$")

    plt.plot(time, quantity, color=color, ls=ls, lw=2.5)

    c_counter1+=1

sns.set_style("whitegrid")
sns.despine(ax=ax1, top=True, right=True, left=False, bottom=False)
sns.set(style="ticks", font_scale=fscale)

xticks      = [ 0.2, 0.3, 0.5, 1, 2, 3, 5 ] # 0.0, 0.1, 0.2, 
xticklabels = [ "0.2", "0.3", "0.5", "1", "2", "3", "5" ] # "0.0", "0.1", "0.2", 
yticks      = [ 0.01, 0.02, 0.03, 0.05, 0.1, 0.2, 0.3, 0.5, 1 ]
yticklabels = [ str(round(i*100)) for i in yticks ]

# ax1.text(0.02, 0.98, 'B', color="k", rotation=0, ha="left", va="top", fontsize=fsize+10, transform=ax1.transAxes, bbox=dict(fc='white', ec="white", alpha=0.01, pad=0.1, boxstyle='round'))

txt1_x  = 0.45
txt1_y  = 0.2
txt_co  = ax1.text(txt1_x, txt1_y, r'CO', color=qred, rotation=0, ha="left", fontsize=fsize_l, transform=ax1.transAxes)
txt_h2o = ax1.text(txt1_x, txt1_y-0.07, r'H$_\mathrm{2}$O', color=qblue, rotation=0, ha="left", fontsize=fsize_l, transform=ax1.transAxes)
txt_co2 = ax1.text(txt1_x, txt1_y-0.14, r'CO$_\mathrm{2}$', color=qgreen, rotation=0, ha="left", fontsize=fsize_l, transform=ax1.transAxes)

plt.xscale("log")
plt.yscale("log")
plt.xlim(left=np.min(xticks), right=np.max(xticks))
plt.ylim(top=np.max(yticks), bottom=np.min(yticks))

ax1.set_xticks( xticks )
ax1.set_xticklabels( xticklabels, fontsize=fsize_m )
ax1.set_yticks( yticks )
ax1.set_yticklabels( yticklabels, fontsize=fsize_m )

legend = ax1.legend(loc=3, fontsize=fsize_s, ncol=1, title=r"$R_\mathrm{P}$, $^{26}$Al") # , title=r"$R_\mathrm{P}$, $^{26}$Al"
plt.setp(legend.get_title(), fontsize=fsize-2)

plt.ylabel(r"Retained volatile fraction, $f_{\mathrm{vol}}$ (vol%)", fontsize=fsize_l)
plt.xlabel(r"Time after planetesimal formation, $t_\mathrm{plts}$ (Myr)", fontsize=fsize_l)

figure_name="fig_plts_time"+".pdf"
plt.savefig(fig_dir+"/21_Lichtenberg_Krijt/"+figure_name, bbox_inches='tight')
