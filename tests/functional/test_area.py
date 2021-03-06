test_area = {
    'name':'Testing area',
    'area_type':'field',
    'vocabulary': {
        'id':None,
        'resource':'taxonomy_vocabulary'
    }
}

#
# Test farm area methods
#
def test_create_area(test_farm):
    # Find the vocab ID for farm_areas
    farm_areas_id = test_farm.vocabulary('farm_areas')[0]['vid']

    # Update the test_area with the vid
    test_area['vocabulary']['id'] = farm_areas_id

    response = test_farm.area.send(test_area)
    print(test_area, response)
    assert 'id' in response

    # Once created, add 'id' to test_asset
    test_area['id'] = response['id']

def test_get_all_farm_areas(test_farm):
    areas = test_farm.area.get()

    assert 'list' in areas
    assert 'page' in areas
    assert len(areas) > 0
    

def test_get_farm_areas_filtered_by_type(test_farm):
    area_type = test_area['area_type']

    areas = test_farm.area.get({
        'area_type':area_type
    })

    assert len(areas) > 0
    assert areas['list'][0]['area_type'] == area_type

def test_get_farm_areas_by_id(test_farm):
    area_tid = test_area['id']
    areas = test_farm.area.get(int(area_tid))
    area = areas['list'][0]

    assert 'tid' in area
    assert area['tid'] == area_tid

def test_update_area(test_farm):
    test_area_changes = {
        'id':test_area['id'],
        'name':'Area changed name'
    }
    response = test_farm.area.send(test_area_changes)
    assert 'id' in response
    assert response['id'] == test_area['id']

    updated_area = test_farm.area.get(int(test_area['id']))
    assert updated_area['list'][0]['name'] == test_area_changes['name']

def test_delete_area(test_farm):
    response = test_farm.area.delete(int(test_area['id']))
    assert response.status_code == 200
