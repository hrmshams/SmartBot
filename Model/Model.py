from .TvPlans import TvPlans


class Model:

    @staticmethod
    def get_tv_plans(channel_name):
        tv_plan = TvPlans()
        result = tv_plan.get_tv_plans(TvPlans.get_channel_names()[channel_name])

        plans_name = result[2]
        plans_start = result[0]
        plans_end = result[1]

        text = "📺 برنامه های " + channel_name + " 📺" + "\n\n"
        text = text + "نام برنامه" + " | " + "تاریخ شروع" + " | " + "تاریخ پایان" + "\n"

        for i in range(0, len(plans_name)):
            text = text + plans_name[i] + " :\n" + "<code>" + " | " + plans_start[i] + " | " + plans_end[i] + " | " + "</code>" + "\n"

        text = text + "\n" + "@casscobot"

        return text
