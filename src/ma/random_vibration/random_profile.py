import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter


class RandomProfile:
    def __init__(
            self,
            f,
            y,
            name=None,
            description=None,
            ):
        
        self.f = f
        self.y = y
        self.name = name
        self.description = description

    def __log_interp1d(xx, yy, kind='linear'):
        logx = np.log10(xx)
        logy = np.log10(yy)
        lin_interp = sp.interpolate.interp1d(logx, logy, kind=kind)
        log_interp = lambda zz: np.power(10.0, lin_interp(np.log10(zz)))
        
        return log_interp

    def interpolate(self, values):
        interp = self.__log_interp1d(self.f, self.y, kind='linear')
        return interp(values)
    
    def rms_accel(self):

        area = []
        for i in range(1, len(self.f)):

            a_0 = self.y[i-1]
            a_1 = self.y[i]
            f_0 = self.f[i-1]
            f_1 = self.f[i]

            b = np.log(a_1 / a_0) / np.log(f_1 / f_0)

            if b == -1:
                area.append(f_0 * a_0 * np.log(f_1/f_0))
            else:
                area.append((f_1 * a_1 - f_0 * a_0) / (b + 1))
        
        return np.sqrt(np.sum(area))
    
    def plot(self, ax=None, lw=2.0, color='black'):

        if ax is None:
            fig, ax = plt.subplots(figsize=(6,4))

            ax.loglog(self.f, self.y, lw=lw, color=color)
            ax.grid(color='black', which='both', alpha=0.5)
            
            ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
            ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

            ax.set_ylim(bottom=min(self.y)/5, top=max(self.y)*2)

            ax.set_xlabel('Frequency (Hz)')
            ax.set_ylabel('Acceleration (g$^2$/Hz)')

            if self.name is None:
                plt.title('Random vibration PSD')
            else:
                plt.title(self.name)

        else:
            ax.loglog(self.f, self.y, lw=lw, color=color)


if __name__ == "__main__":

    random_min_workmanship = RandomProfile(f=[20., 160., 250., 2000.],
                                           y=[.01, .08, .08, .01],
                                           name='GEVS minimum workmanship'
                                           )

    print(random_min_workmanship.rms_accel())
    random_min_workmanship.plot(color='black')
