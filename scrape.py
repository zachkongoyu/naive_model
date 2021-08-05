from liveEvaluation import stream
import time

chinaamc = stream(160325)
fullgoal = stream(161040)
bosera = stream(501082)
efund = stream(506002)

def scrape(interval, times):

	now=time.time()
	cur_times = 0

	while cur_times != times:

		end = time.time()

		chinaamc.get_evaluation()
		chinaamc.to_df()
		chinaamc.df.to_csv('160325_NAV.csv')

		fullgoal.get_evaluation()
		fullgoal.to_df()
		fullgoal.df.to_csv('161040_NAV.csv')

		bosera.get_evaluation()
		bosera.to_df()
		bosera.df.to_csv('501082_NAV.csv')

		efund.get_evaluation()
		efund.to_df()
		efund.df.to_csv('506002_NAV.csv')

		cur_times += 1

		time.sleep(interval)


if __name__ == '__main__':

	scrape(0, 9)