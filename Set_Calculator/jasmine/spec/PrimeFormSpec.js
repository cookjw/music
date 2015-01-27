describe("Prime Form Calculator", function() {
    it("expects something to do something", function(){
        expect(true).toBe(true);
    });
    it("expects normalMod to work", function() {
        expect(normalMod(-1, 12)).toEqual(11);
    });        
    it("expects at least to be able to copy arrays...", function(){
        expect(copy([1,2,3])).toEqual([1,2,3]);
    });
    it("expects removeDuplicates function to work", function(){
        expect(removeDuplicates([1,2,3])).toEqual([1,2,3]);
        expect(removeDuplicates([1,2,3,3,4])).toEqual([1,2,3,4]);
    });
    it("expects rotate function to work", function() {
        expect(rotate([1,2,3], 1)).toEqual([2,3,1]);
        expect(rotate([1,2,3], 2)).toEqual([3,1,2]);
        expect(rotate([1,2,3], 3)).toEqual([1,2,3]);
    });
    it("expects distance function to work", function() {
        expect(distance([0,1,9])).toEqual(9);
        expect(distance([4,6,3])).toEqual(11);
    });
    it("expects tiebreaker to work", function() {
        expect(tiebreaker([[0,4,6,8],[4,6,8,12]], 4)).toEqual([4,6,8,12]); 
    });        
    // it("expects findPrimeForm to work", function() {
        // // expect(findPrimeForm([0,3,4])).toEqual([0,1,4]);
    // });    
    // it("", function() {
        // expect().toEqual()
    // });        
    // it("", function() {
        // expect().toEqual()
    // it("", function() {
    // }); 
});