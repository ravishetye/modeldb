import * as R from 'ramda';

import checkURLSearchParams from 'shared/utils/tests/checkURLSearchParams';
import flushAllPromises from 'shared/utils/tests/integrations/flushAllPromises';
import routes from 'shared/routes';
import setupIntegrationTest from 'shared/utils/tests/integrations/setupIntegrationTest';
import { userWorkspacesWithCurrentUser } from 'shared/utils/tests/mocks/models/workspace';

import {
  changeProjectsPaginationWithLoading,
  getDefaultProjectsOptions,
} from '../actions';
import { selectProjectsPagination } from '../selectors';
import { loadProjectsActionTypes } from '../types';

describe('store', () => {
  beforeEach(() => {
    localStorage.clear();
  });

  describe('projects', () => {
    describe('pagination', () => {
      const runChangePagination = async (currentPage: number) => {
        const integrationTestData = setupIntegrationTest({});
        integrationTestData.store.dispatch(changeProjectsPaginationWithLoading(
          currentPage,
          [],
          userWorkspacesWithCurrentUser.user.name
        ) as any);
        await flushAllPromises();
        return integrationTestData;
      };

      it('should correct change current page in store', async () => {
        const { store } = await runChangePagination(2);

        expect(selectProjectsPagination(store.getState()).currentPage).toEqual(
          2
        );
      });

      it('should load projects with new pagination', async () => {
        const { dispatchSpy } = await runChangePagination(2);
        await flushAllPromises();

        expect(
          R.flatten(dispatchSpy.mock.calls).some(
            ({ type }: any) => type === loadProjectsActionTypes.REQUEST
          )
        ).toBe(true);
      });

      describe('saving pagination in URL', () => {
        const changeAndCheckCurrentPageInURL = async (
          newCurrentPage: number,
          expectedCurrentPageInURL: string | null
        ) => {
          const { history } = await runChangePagination(newCurrentPage);
          checkURLSearchParams(history, { page: expectedCurrentPageInURL });
        };

        it('should display incremented current page', async () => {
          await changeAndCheckCurrentPageInURL(2, '3');
          await changeAndCheckCurrentPageInURL(3, '4');
        });

        it('should delete current page if current page is the first page', async () => {
          await changeAndCheckCurrentPageInURL(0, null);
        });
      });

      describe('restoring pagination from URL', async () => {
        const { store } = setupIntegrationTest({
          pathname: `${routes.projects.getRedirectPath({
            workspaceName: userWorkspacesWithCurrentUser.user.name,
          })}?page=${3}`,
        });

        await store.dispatch(getDefaultProjectsOptions() as any);

        expect(selectProjectsPagination(store.getState()).currentPage).toEqual(
          2
        );
      });
    });
  });
});
