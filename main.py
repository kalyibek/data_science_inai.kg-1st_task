import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import time


matplotlib.use('TkAgg')

def exercise_e_f(data):
    print("-----------------EXERCISE E & F-------------")

    format_for_parsing = '%Y%m%d%H'
    format_of_datetime_index = '%Y-%m-%d %H:00:00'

    start_date = time.strftime(
        format_of_datetime_index,
        time.strptime(
            data.iloc[0]['datetime'],
            format_for_parsing
        )
    )

    end_date = time.strftime(
        format_of_datetime_index,
        time.strptime(
            data.iloc[-1, :]['datetime'],
            format_for_parsing
        )
    )

    data.index = pd.date_range(
        start=start_date,
        end=end_date,
        freq="1H"
    )

    data[['temperature']] = data[['temperature']].astype(float)

    data.drop(
        ['id', 'datetime', 'qn_9', 'rf_tu', 'eor'],
        axis=1,
        inplace=True
    )

    print(data)
    exercise_g(data)


def exercise_g(data):
    print("-----------------EXERCISE G-------------")
    print("{Temperature change as a percentage relative to the previous value}\n")

    data['relation to the previous value'] = data.pct_change(data["temperature"].any())

    print(data)

    min_temperature = data['temperature'].min()
    max_temperature = data['temperature'].max()
    average_temperature = data['temperature'].mean()
    median_temperature = data['temperature'].median()

    print(
        'The default statistics:',
        f'Maximum temperature value - {max_temperature}',
        f'Minimum temperature value - {min_temperature}',
        f'Average temperature value - {round(average_temperature, 2)}',
        f'Median temperatures - {median_temperature}',
        sep='\n'
    )

    exercise_h_i_j(data)


def exercise_h_i_j(data):
    data.drop(
        ['relation to the previous value'],
        axis=1,
        inplace=True
    )

    qty_of_plots = 3
    qty_of_plots_in_column = 1

    # plot1 (All):
    x = data.index
    y = data['temperature']
    plt.subplot(qty_of_plots, qty_of_plots_in_column, 1)
    plt.plot(x, y)
    plt.title("Temperature chart for all time")
    plt.xlabel("Datetime")
    plt.ylabel("Temperature")

    # plot2 (Temperature for 1 month)
    y = data.loc['2016-04-01 00:00:00':'2016-04-30 23:00:00']
    print(y)
    plt.subplot(qty_of_plots, qty_of_plots_in_column, 2)
    plt.plot(y, color='gold')
    plt.title("Temperature chart for April")
    plt.xlabel("Datetime")
    plt.ylabel("Temperature")

    # plot3 (Temperature for June 2017 higher than 25)
    june_2017 = data.loc['2017-06-01 00:00:00':'2017-06-30 23:00:00']
    y = june_2017[june_2017['temperature'] > 25]
    plt.subplot(qty_of_plots, qty_of_plots_in_column, 3)
    plt.plot(y, color='orange')
    plt.title("Temperature chart for June 2017")
    plt.xlabel("Datetime")
    plt.ylabel("Temperature")

    plt.subplots_adjust(wspace=1, hspace=1)
    plt.show()


if __name__ == '__main__':
    print("-----------------EXERCISE D-------------")
    data = pd.read_csv(
        "temp_fuhlsbuettel_akt.txt",
        delimiter=";",
        names=[
            'id',
            'datetime',
            'qn_9',
            'temperature',
            'rf_tu',
            'eor'
        ],
    )

    dataframe = pd.DataFrame(data)
    dataframe.drop(index=[0], axis=0, inplace=True)
    print(dataframe)

    exercise_e_f(dataframe)
