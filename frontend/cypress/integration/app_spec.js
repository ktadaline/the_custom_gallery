describe("Django REST framework / React quickstart app", () => {
    const art = {
        art_title: "I'm Blue",
        art_description: "58\" x 90\"",
        art_completion_date: "June 2008",
        medium: "Acrylic, Canvas",
        art_image: "https://images.fineartamerica.com/images/artworkimages/mediumlarge/1/never-alone-sharon-cummings.jpg",
        file_type: "jpg",
        created_at: "2018-09-27T00:00:00",
        artist: 1
    };

    before(() => {
        cy.exec("npm run dev");
        cy.exec("npm run flush");
    });

    it("should be able to fill a web form", ()=>{
        cy.visit("/");

        cy
            .get('input[name="art_title"]')
            .type(art.art_title)
            .should("have.value", art.art_title);

        cy
            .get('input[name="art_description"]')
            .type(art.art_description)
            .should("have.value", art.art_description);

        cy
            .get('input[name="art_completion_date"]')
            .type(art.art_completion_date)
            .should("have.value", art.art_completion_date);

        cy
            .get('input[name="medium"]')
            .type(art.medium)
            .should("have.value", art.medium);

        cy
            .get('input[name="art_image"]')
            .type(art.art_image)
            .should("have.value", art.art_image);

        cy
            .get('input[name="file_type"]')
            .type(art.file_type)
            .should("have.value", art.file_type);

        cy
            .get('input[name="created_at"]')
            .type(art.created_at)
            .should("have.value", art.created_at);

        cy
            .get('input[name="artist"]')
            .type(art.artist)
            .should("have.value", art.artist);

        cy.get("form").submit();

    });

    //more tests here
});