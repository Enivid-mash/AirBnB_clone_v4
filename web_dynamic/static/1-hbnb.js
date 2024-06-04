$(document).ready(function() {
  const selectedAmenities = {};

  $('li input[type="checkbox"]').change(function() {
    const amenityName = $(this).data('name');
    const amenityId = $(this).data('id');

    if (this.checked) {
      selectedAmenities[amenityName] = amenityId;
    } else {
      delete selectedAmenities[amenityName];
    }

    const sortedNames = Object.keys(selectedAmenities).sort();
    const joinedNames = sortedNames.join(", ");
    $('.amenities h4').text(joinedNames);
  });
});

