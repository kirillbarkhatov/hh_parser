# from unittest.mock import patch, mock_open
#
#
#
#
#
# @patch("pandas.read_excel")
# def test_get_transactions_from_xls(mock_read_excel, dict_for_pd_as_xls, dict_for_pd_for_working):
#     m = mock_open()
#     mock_read_excel.return_value = pd.DataFrame(dict_for_pd_as_xls)
#     result = pd.DataFrame(dict_for_pd_for_working)
#     with patch("builtins.open", m):
#         assert result.equals(get_transactions_from_xls("test"))
#         mock_read_excel.assert_called_once_with("test")
#
