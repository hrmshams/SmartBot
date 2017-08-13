from .TvPlans import TvPlans

class Model:

    @staticmethod
    def get_tv_plans(self):
        tv_plan = TvPlans()
        result = tv_plan.get_tv_plans()
