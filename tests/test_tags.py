from opentypespec.tags import FEATURE_TAGS

def test_features():
	assert "liga" in FEATURE_TAGS
	assert "lig " not in FEATURE_TAGS
	assert FEATURE_TAGS["cv03"]["name"] == "Character variant 3"
