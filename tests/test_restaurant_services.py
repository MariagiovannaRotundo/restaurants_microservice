from services import RestaurantService


class TestRestaurantsServices:
    def test_all_restaurant(self):
        """
        test about the services restaurant to test the result of all restaurants
        :return:
        """
        all_restaurants = RestaurantService.get_all_restaurants()
        assert len(all_restaurants) == 2
